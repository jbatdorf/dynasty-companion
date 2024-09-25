import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import "./models/Players";
import { getAllPlayers } from "./models/Players";
import { Player } from "./models/Players.types";

function App() {
  const [players, setPlayers] = useState<Player[] | null>(null);

  return (
    <>
      <h1>Enter your league ID</h1>
      <div className="card">
        <label id="league-id">
          <input id="league-id"></input>
        </label>
        <button
          onClick={() => {
            /* go to league page */
          }}
        >
          GO
        </button>
        {players?.map((player) => {
          return (
            <li key={player.id}>
              {player.name} - {player.position} - {player.team}
            </li>
          );
        })}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
