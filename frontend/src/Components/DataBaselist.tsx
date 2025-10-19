import { Table } from "react-bootstrap";

interface DataItem {
  fecha: string;
  precioA: number;
  precioO: number;
  descuento: number;
  Disponibilidad: boolean;
}

interface Props {
  data: DataItem[];
}

const dataBaselist = ({ data }: Props) => {
  let color = false;
  return (
    <div>
      <Table className="table table-sm table-hover">
        <thead>
          <tr>
            <th>Fecha/Hora</th>
            <th>Precio Actual</th>
            <th>Precio Original</th>
            <th>Descuento</th>
            <th>Disponibilidad</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index} className={color ? "table-secondary" : ""}>
              {(color = !color)}
              <td>{item.fecha}</td>
              <td>${item.precioA.toLocaleString()}</td>
              <td>${item.precioO.toLocaleString()}</td>
              <td>
                <span
                  className={`badge text-bg-${
                    item.descuento >= 0 ? "success" : "danger"
                  }`}
                >
                  {item.descuento}%
                </span>
              </td>
              <td>
                <span
                  className={`badge text-bg-${
                    item.Disponibilidad ? "success" : "danger"
                  }`}
                >
                  {item.Disponibilidad ? "disponible" : "no disponible"}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default dataBaselist;
