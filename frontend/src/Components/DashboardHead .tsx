import { Card, Col, Row } from "react-bootstrap";

interface Props {
  precio: number;
  Descuento: number;
  Promedio: number;
  Registros: number;
}

const Dashboard_head = (props: Props) => {
  const { precio, Descuento, Promedio, Registros } = props;
  return (
    <>
      <Row className="mb-4">
        <Col clasName="p-0">
          <Card className="bg-success text-light text-center p-0 shadow h-100">
            <Card.Header className="border-bottom h-50 text-center">
              Precio Actual
            </Card.Header>
            <Card.Body>${precio.toLocaleString()}</Card.Body>
          </Card>
        </Col>
        <Col clasName="p-0">
          <Card className="bg-info text-light text-center p-0 shadow h-100">
            <Card.Header className="border-bottom h-50 text-center">
              Descuento
            </Card.Header>
            <Card.Body>{Descuento}</Card.Body>
          </Card>
        </Col>
        <Col clasName="p-0">
          <Card className="bg-warning text-light text-center p-0 shadow h-100">
            <Card.Header className="border-bottom h-50 text-center">
              Precio Promedio
            </Card.Header>
            <Card.Body>${Promedio.toLocaleString()}</Card.Body>
          </Card>
        </Col>
        <Col clasName="p-0">
          <Card className="bg-secondary text-light text-center p-0 shadow border h-100">
            <Card.Header className="border-bottom h-50 text-center">
              Registros
            </Card.Header>
            <Card.Body>{Registros}</Card.Body>
          </Card>
        </Col>
      </Row>
    </>
  );
};

export default Dashboard_head;
