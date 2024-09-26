import "./App.css";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import * as ReactDOM from "react-dom/client";
import React from "react";
import Home from "./routes/Home/Home";

function App() {
    const router = createBrowserRouter([
        {
            path: "/",
            element: <Home />,
            children: [
                {
                    path: "/:leagueId",
                    element: <div>your league!</div>,
                },
            ],
        },
    ]);

    ReactDOM.createRoot(document.getElementById("root")!).render(
        <React.StrictMode>
            <RouterProvider router={router} />
        </React.StrictMode>,
    );
}

export default App;
