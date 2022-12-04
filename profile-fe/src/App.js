import React, { useContext } from "react";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";
import axios from "axios";

import { ThemeContext } from "./contexts/ThemeContext";
import { Main, BlogPage, ProjectPage } from "./pages";
import { BackToTop } from "./components";
import ScrollToTop from "./utils/ScrollToTop";

import "./App.css";

function App() {
  const { theme } = useContext(ThemeContext);

  console.log(
    "%cANUSHKA PORTFOLIO",
    `color:${theme.primary}; font-size:50px`
  );
  console.log(
    "%chttps://github.com/Aditya-Anshul",
    `color:${theme.tertiary}; font-size:20px`
  );
  // console.log = console.warn = console.error = () => {};
  
 /*
  let data;
        axios
            .get("http://localhost:8000/")
            .then((res) => {
                data = res.data;
                this.setState({
                    details: data,
                });
            })
            .catch((err) => {});
 */
 
      // <Route path="/blog" exact component={BlogPage} />

  return (
    <div className="app">
      <Router>
        <ScrollToTop />
        <Switch>
          <Route path="/" exact component={Main} />

          <Route path="/projects" exact component={ProjectPage} />

          <Redirect to="/" />
        </Switch>
      </Router>
      <BackToTop />
    </div>
  );
}

export default App;
