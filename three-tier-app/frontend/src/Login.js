import React, { useState } from "react";
import API from "./api";


export default function Login({ setToken }) {
const [username, setUsername] = useState("");
const [password, setPassword] = useState("");


const login = async () => {
try {
const res = await API.post("/login", { username, password });
if (res.data.status === "ok") {
setToken(res.data.data.token);
} else {
alert(res.data.message || "Login failed");
}
} catch (e) {
alert("Login failed: " + e.message);
}
};


return (
<div style={{ margin: 20 }}>
<h2>Login</h2>
<input
placeholder="Username"
value={username}
onChange={(e) => setUsername(e.target.value)}
/>
<br /><br />
<input
placeholder="Password"
type="password"
value={password}
onChange={(e) => setPassword(e.target.value)}
/>
<br /><br />
<button onClick={login}>Login</button>
</div>
);
}
