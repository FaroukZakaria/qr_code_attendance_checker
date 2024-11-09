var lastResult = 0;
async function onScanSuccess(decodedText) {
if (decodedText !== lastResult) {
    lastResult = decodedText;
    const response = await fetch("/record-attendance", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        id: decodedText,
    }),
    });
    const data = await response.json();
    alert(data.message);

    html5QrcodeScanner.clear();
}
}
function onScanError(errorMessage) {
// handle scan error (For future development, probably not needed)
}

var html5QrcodeScanner = new Html5QrcodeScanner("reader", {
fps: 10,
qrbox: 250,
});
html5QrcodeScanner.render(onScanSuccess, onScanError);