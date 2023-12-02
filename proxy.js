const app = require("express")();

app.get("/", (req, res) => {
  res.send("This is my proxy");
  console.log("Received request for host" + req.hostname);
});

app.listen(8080, () => {
  console.log("Listening on port 8080");
});
