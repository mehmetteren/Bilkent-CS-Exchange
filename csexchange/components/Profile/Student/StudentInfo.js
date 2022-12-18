import { useState } from "react";
import { Button, Col, Row, Card, Modal } from "react-bootstrap";
import Link from "next/link";
import { useSelector } from "react-redux";

const StudentInfo = (props) => {
  const [show, setShow] = useState(false);
  const handleShow = () => {
    setShow(true);
  };
  const handleClose = () => {
    setShow(false);
  };

  const user = useSelector((state) => state.auth.bilkentId);

  return (
    <Card className="p-2">
      <Col>
        <Row>
          <h1>INFO</h1>
        </Row>
        <Row className="mt-3 pb-5">
          <Col className="col-6">
            <h4>University: {props.universityName} </h4>
          </Col>
          <Col className="col-3">
            <Button variant="secondary">Go To University Page</Button>
          </Col>
          <Col className="col-3">
            <Button variant="danger" onClick={handleShow}>
              Cancel Application
            </Button>
          </Col>
        </Row>
        <Row className="mt-5 pb-5">
          <Col className="col-6">
            <h4>Coordinator: {props.coordinator}</h4>
          </Col>
          <Col className="col-3">
            <Button variant="secondary">Go To Coordinator Profile</Button>
          </Col>
          <Col className="col-3">
            <Button variant="secondary">Send Message</Button>
          </Col>
        </Row>
        <Row className="mt-5 pb-5">
          <Col className="col-6">
            <h4>Department Secretary: {props.departmentSecretary}</h4>
          </Col>
          <Col className="col-3">
            <Button variant="secondary">Go To Secretary Profile</Button>
          </Col>
          <Col className="col-3">
            <Button variant="secondary">Send Message</Button>
          </Col>
        </Row>
        <Row className="mt-5">
          <Col className="col-4 d-flex justify-content-center align-items-center">
            <Link href={`/student/preapproval/${user}`} passHref legacyBehavior>
              <Button variant="success" size="lg">
                Fill Pre-Approval
              </Button>
            </Link>
          </Col>
          <Col className="col-4 d-flex justify-content-center align-items-center">
            <Link href={`/student/learningagreement/${user}`} passHref legacyBehavior>
              <Button variant="success" size="lg">
                Fill Learning Agreement
              </Button>
            </Link>
          </Col>
          <Col className="col-4 d-flex justify-content-center align-items-center">
          <Link href={`/student/files/${user}`} passHref legacyBehavior>
              <Button variant="success" size="lg">
                Go to Files
              </Button>
            </Link>
          </Col>
        </Row>
      </Col>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Warning</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <h5>
            You have to contact with your department coordinator to cancel your
            application!
          </h5>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </Card>
  );
};

export default StudentInfo;