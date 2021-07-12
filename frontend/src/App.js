import { Container } from "react-bootstrap";
import { BrowserRouter as Router } from "react-router-dom";
import Sidebar from "./components/Sidebar/Sidebar";
import "./App.css";

function App() {
  return (
    <div className="App bg-dark">
      <Router>
        <Sidebar />
      </Router>
    </div>
  );
}

export default App;
