import DashboardHead from "./Components/DashboardHead ";
import ResumenGeneral from "./Components/ResumenGeneral";

function App() {
  return (
    <>
      <div className="bg-primary text-white p-4 ">
        <h1>Dashboard dw </h1>
      </div>

      <main className="p-2">
        <DashboardHead
          precio={2000}
          Descuento={15}
          Promedio={2500}
          Registros={5}
        />
        <ResumenGeneral />
      </main>
    </>
  );
}

export default App;
