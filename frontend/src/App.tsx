import DashboardHead from "./Components/DashboardHead ";
import Historico from "./Components/Historico";
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
        <ResumenGeneral
          Producto="Arroz diana"
          Descripcion="pvt0"
          PrecioOriginal={5000}
          Disponibilidad
          Actualizacion="hoy"
          precioMax={15165}
          precioMin={5564}
          ProductoLink="https://www.google.com/"
        />
        <Historico />
      </main>
      <footer>
        <div className="row mt-4">
          <div className="col text-center text-muted">
            <small id="ultima-actualizacion-footer">
              Dashboard web - Monitoreo de Precios | Actualizado: hoy
            </small>
          </div>
        </div>
      </footer>
    </>
  );
}

export default App;
