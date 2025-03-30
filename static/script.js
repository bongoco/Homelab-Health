function updateStatus() {
    fetch('/status')
        .then(response => response.json())
        .then(data => {
            document.getElementById("status_pi").textContent = "Pi-Hole: " + data.server_pi;
            document.getElementById("status_hp").textContent = "HP Elitedesk: " + data.server_hp;
            document.getElementById("status_ubuntu").textContent = "Ubuntu VM: " + data.vm_ubuntu;

            document.getElementById("status_pi").className = "status " + (data.server_pi.includes('UP') ? 'up' : 'down');
            document.getElementById("status_hp").className = "status " + (data.server_hp.includes('UP') ? 'up' : 'down');
            document.getElementById("status_ubuntu").className = "status " + (data.vm_ubuntu.includes('UP') ? 'up' : 'down');
        });
}

document.addEventListener("DOMContentLoaded", function () {
    updateStatus();
    setInterval(updateStatus, 1000); // refresh every 1 sec
});
