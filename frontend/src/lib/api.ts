const API_BASE = "https://late-night-radio.onrender.com";

export async function saveVisitor(name: string) {
  const response = await fetch(`${API_BASE}/visitors`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to save visitor");
  }

  return response.json();
}

export async function saveThought(text: string) {
  const response = await fetch(`${API_BASE}/thoughts`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to save thought");
  }

  return response.json();
}
