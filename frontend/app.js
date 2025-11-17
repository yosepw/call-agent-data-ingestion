const apiBase = "/api";

document.getElementById("btn-onboard").onclick = async () => {
  const payload = {
    name: document.getElementById("trunk-name").value,
    sip_url: document.getElementById("sip-url").value,
    username: document.getElementById("username").value,
    password: document.getElementById("password").value,
  };
  const res = await fetch(\${apiBase}/sip/onboard, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const text = await res.text();
  document.getElementById("onboard-res").textContent = text;
};

document.getElementById("btn-start").onclick = async () => {
  const payload = {
    task_id: document.getElementById("task-id").value,
    script: document.getElementById("script").value,
    concurrency: parseInt(document.getElementById("concurrency").value || "1"),
  };
  const res = await fetch(\${apiBase}/call/start, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const text = await res.text();
  document.getElementById("start-res").textContent = text;
};
