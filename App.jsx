import "./App.css";
import {BarChart, Bar, XAxis, YAxis, Tooltip} from "recharts";
const data = [
{name:"Jan", dose:400},
{name:"Feb", dose:700},
{name:"Mar", dose:900}
];
function CowinDashboard(){
return (
<div className="dashboard">
<h2>CoWIN Dashboard</h2>
<div className="chart-container">
<BarChart width={400} height={300} data={data}>
<XAxis dataKey="name"/>
<YAxis/>
<Tooltip/>
<Bar dataKey="dose" fill="#4facfe"/>
</BarChart>
</div>
</div>
);
}
export default CowinDashboard;
