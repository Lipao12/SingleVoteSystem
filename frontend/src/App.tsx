import { useEffect, useState } from "react";
import { api } from "./lib/axios";

interface Candidate {
  id: string;
  name: string;
  vote_qnt: number;
}

function App() {
  const [candidates, setCandidates] = useState<Candidate | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.post("/candidates", {
          columns: [],
        });
        setCandidates(response.data);
      } catch (err) {
        console.log(err);
      }
    };

    fetchData();
  }, []);

  console.log(candidates);

  return (
    <div>
      {candidates ? (
        <ul>
          {candidates.map((candidate: Candidate) => (
            <li key={candidate.id}>{candidate.name}</li>
          ))}
        </ul>
      ) : (
        <p>Carregando candidatos...</p>
      )}
    </div>
  );
}

export default App;
