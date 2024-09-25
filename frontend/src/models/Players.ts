import React from "react";
import axios from "axios";
import { Player } from "./Players.types";

const BASE_URL = "http://localhost:3000";

export const getAllPlayers = async (): Promise<Player[]> => {
  return (await axios.get(`${BASE_URL}/players`)).data;
};
