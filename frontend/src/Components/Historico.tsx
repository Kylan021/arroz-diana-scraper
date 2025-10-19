import { Card } from "react-bootstrap";
import DataBaselist from "./dataBaselist";
interface Props {
  dataBase: Array<any>;
}

const Historico = (props: Props) => {
  return (
    <>
      <Card className="mt-2">
        <Card.Header className="text-center">Historico</Card.Header>
        <Card.Body className="overflow-y-scroll" style={{ height: "300px" }}>
          <DataBaselist data={props.dataBase} />
        </Card.Body>
      </Card>
    </>
  );
};

export default Historico;
