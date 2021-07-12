import { useState } from "react";
import { Link } from "react-router-dom";
import "./Sidebar.css";

const Sidebar = () => {
  const [sidebar, setSidebar] = useState(false);
  const showSidebar = () => setSidebar(!sidebar);

  return (
    <nav
      className={
        sidebar ? "sidebar active bg-secondary" : "sidebar bg-secondary"
      }
    >
      <button
        className="hamburger bg-secondary"
        type="button"
        onClick={showSidebar}
      >
        <div></div>
      </button>
      <ul onClick={showSidebar}>
        <li>
          <Link to="/">Home</Link>
          <Link to="/">Profile</Link>
          <Link to="/">Draft</Link>
          <Link to="/">About</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Sidebar;
