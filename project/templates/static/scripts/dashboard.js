let userName;
let admin;
document.addEventListener("DOMContentLoaded", async function () {
const response = await fetch("/check-auth");
if (response.status === 401) {
    alert("Access token is invalid or expired. Please log in again.");
    await fetch("/signout", {
    method: "GET",
    });
    window.location.href = "/signin";
    return;
}
const data = await response.json();
userName = data.name;
admin = data.admin;


if (admin) {
    document.getElementsByClassName("admin")[0].innerHTML = `
    <p>Welcome, ${userName}</p>
    <!-- will add buttons for admin actions here -->
    `;
} else {
    document.getElementsByClassName("student")[0].innerHTML =`
      <div class="scanner">
        <div style="width: 500px" id="reader"></div>
      </div>
      `;
      let script = document.createElement("script");
      script.src = "static/scripts/qr-code.js";
      document.body.appendChild(script);
}
});