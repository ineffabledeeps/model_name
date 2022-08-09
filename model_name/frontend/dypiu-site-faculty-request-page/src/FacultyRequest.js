import { useState } from "react";
import FacultyRequestTable from "./components/facultyRequestTable/facultyRequestTable.component";

import "./styles.css";

export default function FacultyRequest() {
  return (
    <div className="App">
      {/* FacultyRequestTable */}
      <FacultyRequestTable />
    </div>
  );
}
