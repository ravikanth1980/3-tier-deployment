import React, { useState, useEffect } from "react";
import API from "./api";


export default function Orders({ token }) {
const [orders, setOrders] = useState([]);
const [product, setProduct] = useState("");
const [qty, setQty] = useState(1);
const [price, setPrice] = useState(0);


const headers = { Authorization: `Bearer ${token}` };


const loadOrders = async () => {
const res = await API.get("/orders", { headers });
setOrders(res.data.data || []);
};


const createOrder = async () => {
await API.post(
"/orders",
{
product,
quantity: qty,
total_price: price,
},
{ headers }
);
loadOrders();
};


useEffect(() => {
loadOrders();
}, []);


return (
<div style={{ margin: 20 }}>
<h2>Orders</h2>
<input
placeholder="Product"
value={product}
onChange={(e) => setProduct(e.target.value)}
/>
<br /><br />
<input
placeholder="Qty"
type="number"
value={qty}
onChange={(e) => setQty(e.target.value)}
/>
<br /><br />
<input
placeholder="Price"
type="number"
value={price}
onChange={(e) => setPrice(e.target.value)}
/>
<br /><br />
<button onClick={createOrder}>Create Order</button>


<h3>Order List</h3>
<ul>
{orders.map((o) => (
<li key={o.id}>
{o.product} — {o.quantity} — {o.total_price}
</li>
))}
</ul>
</div>
);
}
