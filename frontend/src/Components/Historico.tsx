import { Card } from "react-bootstrap";
import DataBaselist from "./dataBaselist";
interface Props {
  dataBase: Array<any>;
}

const Historico = (props: Props) => {
  return (
    <Card>
      <Card.Header className="text-center">Historico</Card.Header>
      <Card.Body>
        <DataBaselist data={props.dataBase} />
      </Card.Body>
    </Card>
  );
};

export default Historico;
