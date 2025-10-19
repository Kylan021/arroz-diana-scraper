import { Card, Row, Col, Table, Button, Stack } from "react-bootstrap";

interface Props {
  Producto: string;
  PrecioOriginal: number;
  Disponibilidad?: boolean;
  Descripcion: string;
  Actualizacion: string;
  precioMax: number;
  precioMin: number;
  ProductoLink: string;
}

const ResumenGeneral = (props: Props) => {
  const {
    Producto,
    PrecioOriginal,
    Disponibilidad,
    Descripcion,
    Actualizacion,
    precioMax,
    precioMin,
    ProductoLink,
  } = props;

  return (
    <>
      <Row md={12}>
        <Col md={7}>
          <Card className="h-100">
            <Card.Header>informacion del Producto</Card.Header>
            <Card.Body>
              <Table className="striped bordered responsive hover">
                <tbody>
                  <tr className="table-secondary">
                    <th>Producto:</th>
                    <td>{Producto}</td>
                  </tr>
                  <tr>
                    <th>Precio Original:</th>
                    <td>{PrecioOriginal.toLocaleString()}</td>
                  </tr>
                  <tr className="table-secondary">
                    <th>Disponibilidad:</th>
                    <td>
                      <span
                        className={`badge text-bg-${
                          Disponibilidad ? "success" : "danger"
                        }`}
                      >
                        {Disponibilidad ? "disponible" : "no disponible"}
                      </span>
                    </td>
                  </tr>
                  <tr>
                    <th>Descripcion:</th>
                    <td>{Descripcion}</td>
                  </tr>
                  <tr className="table-secondary">
                    <th>Ultima Actualización:</th>
                    <td>{Actualizacion}</td>
                  </tr>
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
        <Col md={5}>
          <Card>
            <Card.Header>Resumen Estadístico</Card.Header>
            <Card.Body>
              <Table>
                <tbody>
                  <tr>
                    <th>Precio Minimo:</th>
                    <td className="text-success">
                      ${precioMin.toLocaleString()}
                    </td>
                  </tr>
                  <tr>
                    <th>Precio Maximo:</th>
                    <td className="text-danger">
                      ${precioMax.toLocaleString()}
                    </td>
                  </tr>
                  <tr>
                    <th>Tendencia:</th>
                    <td>q</td>
                  </tr>
                </tbody>
              </Table>
            </Card.Body>
          </Card>
          <Card>
            <Card.Header>Acciones</Card.Header>
            <Card.Body className="p-3">
              <Stack gap={2} className="col-md-5 mx-auto">
                <Button href={ProductoLink}>Ver en la web</Button>
                <Button variant="outline-secondary">Cancel</Button>
              </Stack>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </>
  );
};

export default ResumenGeneral;
