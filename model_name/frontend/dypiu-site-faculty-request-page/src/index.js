import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import FacultyRequest from "./FacultyRequest";

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
  <StrictMode>
    <FacultyRequest />
  </StrictMode>
);
