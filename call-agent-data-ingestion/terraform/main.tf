terraform {
  required_version = ">= 1.0.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~=3.0"
    }
  }
}

provider "azurerm" {
  features = {}
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "resource_group" {
  type    = string
  default = "rg-data-ingestion"
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group
  location = var.location
}

resource "azurerm_app_service_plan" "asp" {
  name                = "asp-data-ingestion"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "Linux"
  reserved            = true

  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_container_registry" "acr" {
  name                = "acrdataingest${substr(md5(var.resource_group), 0, 8)}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_linux_web_app" "app" {
  name                = "app-data-ingestion"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_app_service_plan.asp.id

  site_config {
    linux_fx_version = "DOCKER|<ACR_LOGIN_SERVER>/<IMAGE_NAME>:<TAG>"
  }

  app_settings = {
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "DATABASE_URL"                        = "<PLACEHOLDER_CONNECTION_STRING>"
    "API_KEY"                             = "<PLACEHOLDER_API_KEY>"
  }
}

resource "azurerm_postgresql_flexible_server" "db" {
  name                = "pg-data-ingest"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  administrator_login          = "pgadmin"
  administrator_password       = "ChangeThisPassword123!"
  sku_name                     = "B_Standard_B1ms"
  storage_mb                   = 32768
  version                      = "14"
  backup_retention_days        = 7
  geo_redundant_backup_enabled = false
}

resource "azurerm_postgresql_flexible_server_database" "ingestion_db" {
  name                = "ingestiondb"
  resource_group_name = azurerm_resource_group.rg.name
  server_name         = azurerm_postgresql_flexible_server.db.name
}
