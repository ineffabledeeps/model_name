import { useEffect, useState } from "react";
import StudentRequestCards from "./studentRequestCards.component";

import "./facultyRequestTable.styles.css";
import yellowRadialGradient from "../../assets/yellow-radialGradient.png";
import greenRadialGradient from "../../assets/green-radialGradient.png";

import facultyRequestData from "../../data/data.js";

export default function FacultyRequestTable() {
  const [data, setData] = useState(facultyRequestData);

  return (
    <section className="request-table">
      <div className="status-heading">
        <img
          className="status"
          alt="status-radial-gradient"
          src={yellowRadialGradient}
        />

        <h4>Student Request</h4>
      </div>

      {/* available Details */}
      {data.map((detail, i) => {
        if (detail.request === "pending") {
          return (
            <StudentRequestCards
              key={i.toString()}
              className={""}
              detail={detail}
            />
          );
        }
        return null;
      })}

      <div className="status-heading">
        <img
          className="status"
          alt="status-radial-gradient"
          src={greenRadialGradient}
        />

        <h4>Accepted Request</h4>
      </div>

      {/* notAvailable Details */}
      {data.map((detail, i) => {
        if (detail.request === "accepted") {
          return <StudentRequestCards key={i.toString()} detail={detail} />;
        }
        return null;
      })}
    </section>
  );
}
