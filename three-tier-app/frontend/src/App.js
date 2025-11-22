import React, { useState } from "react";
import Login from "./Login";
import Orders from "./Orders";


export default function App() {
const [token, setToken] = useState(null);


return (
<div>
{token ? (
<Orders token={token} />
) : (
<Login setToken={setToken} />
)}
</div>
);
}
