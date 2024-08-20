import { useEffect, useState } from "react";
import { api } from "./lib/axios";

interface Candidate {
  id: string;
  name: string;
  vote_qnt: number;
}

function App() {
  const [candidates, setCandidates] = useState<Candidate[] | null>(null);

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

  return (
    <div className="flex flex-col justify-center items-center min-h-screen space-y-4">
      <p className="text-lg">Escolha um dos candidatos:</p>
      {candidates ? (
        candidates.map((candidate: Candidate) => (
          <div
            className="py-4 px-3 bg-slate-200 w-2/6 text-xl rounded-xl shadow-xl"
            key={candidate.id}
          >
            {candidate.name}
          </div>
        ))
      ) : (
        <p>Carregando candidatos...</p>
      )}
    </div>
  );
}

export default App;
