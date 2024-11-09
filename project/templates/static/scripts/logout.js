function logout() {
    fetch("/signout", {
        method: "GET",
    })
        .then((response) => {
        if (response.ok) {
            window.location.href = "/";
        } else {
            alert("Logout failed.");
        }
        })
        .catch((error) => {
        console.error("Error:", error);
        });
}