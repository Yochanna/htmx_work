import express from "express";
const app = express();

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/users", (req, res) => {
  const users = [
    { id: 1, name: "John Doe" },
    { id: 2, name: "Bob Williams" },
    { id: 3, name: "Shannon Jackson" },
  ];
  res.send(`
    <h2>Users</h2>
    <ul class="list-group">
      ${users.map(u => `<li class="list-group-item">${u.name}</li>`).join("")}
    </ul>
  `);
});

app.listen(3001, () => {
  console.log("Server listening on http://127.0.0.1:3001");
});
