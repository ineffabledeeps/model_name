import studentRequest from "../../assets/student-request.png";

export default function ClassDetails({ detail, className }) {
  const { request, name, prn, year, course, notes } = detail;

  return (
    <article className={`student-card ${className}`}>
      <img src={studentRequest} alt="student-pfp" className="student-pfp" />
      {/* Name & PRN */}
      <div className="student-info">
        <p className="student-name">{name}</p>
        <p className="student-prn">{prn}</p>
      </div>

      {/* Course & Year */}
      <div className="student-course-info">
        <p className="student-course">{course}</p>
        <p className="student-year">{year}</p>
      </div>

      {/* Note title & Note Input */}
      <div className="student-note">
        <p className="note-title">Note</p>
        <textarea type="text" className="note" placeholder="+" />
      </div>

      {/* Buttons */}
      {request === "pending" ? (
        <div className="request-btn-container">
          <button className="accept-btn"> Accept</button>
          <button className="decline-btn">Decline</button>
        </div>
      ) : (
        <button className="contact-btn">Contact</button>
      )}
    </article>
  );
}
