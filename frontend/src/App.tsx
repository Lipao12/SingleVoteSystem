import { useEffect, useState } from "react";
import { MdOutlinePersonOutline } from "react-icons/md";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { api } from "./lib/axios";

interface Candidate {
  id: string;
  name: string;
  vote_qnt: number;
}

function App() {
  const [candidates, setCandidates] = useState<Candidate[] | null>(null);
  const [selectedCandidate, setSelectedCandidate] = useState<string | null>(
    null
  );

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.post("/candidates", {
          columns: [],
        });
        setCandidates(response.data);
      } catch (err) {
        console.log(err);
        toast.error(
          "Erro ao carregar os candidatos. Por favor, tente novamente."
        );
      }
    };

    fetchData();
  }, []);

  const handleCandidateClick = (id: string) => {
    if (selectedCandidate === id) {
      setSelectedCandidate(null);
      return;
    }
    setSelectedCandidate(id);
  };

  const handleConfirmClick = async () => {
    try {
      const response = await api.post("/vote", {
        candidateId: selectedCandidate,
      });
      console.log("Votado: ", response);
      toast.success("Voto registrado com sucesso!");
    } catch (err: any) {
      console.log(err);
      if (err.response) {
        const errorMessage =
          err.response.data.error || "Erro ao registrar o voto.";
        const statusCode = err.response.status;
        toast.error(`Erro ${statusCode}: ${errorMessage}`);
      } else {
        toast.error("Erro desconhecido ao registrar o voto.");
      }
    }
  };

  return (
    <div className="flex flex-col justify-center items-center min-h-screen space-y-4">
      <ToastContainer />
      <p className="text-lg">Escolha um dos candidatos:</p>
      <div className="grid grid-cols-3 gap-4">
        {candidates ? (
          candidates.map((candidate: Candidate) => (
            <div
              onClick={() => handleCandidateClick(candidate.id)}
              className={`py-4 px-3 text-xl rounded-xl shadow-xl text-center flex flex-col items-center space-y-1 cursor-pointer 
                ${
                  selectedCandidate === candidate.id
                    ? "bg-green-500 text-white"
                    : "bg-slate-200"
                }`}
              key={candidate.id}
            >
              <MdOutlinePersonOutline className="text-[50px]" />
              <span>{candidate.name}</span>
            </div>
          ))
        ) : (
          <p className="col-span-3 text-center">Carregando candidatos...</p>
        )}
      </div>
      <button
        onClick={handleConfirmClick}
        disabled={!selectedCandidate}
        className={`mt-4 px-6 py-2 rounded-lg text-lg font-semibold ${
          selectedCandidate
            ? "bg-green-500 text-white"
            : "bg-gray-300 text-gray-600 cursor-not-allowed"
        }`}
      >
        Confirmar escolha
      </button>
    </div>
  );
}

export default App;
