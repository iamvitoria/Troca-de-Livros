function toggleSidebar() {
        var sidebar = document.getElementById("sidebar");
        var content = document.getElementById("content");
        if (sidebar.style.left === "0px") {
            sidebar.style.left = "-220px"; // Fecha a barra lateral
            content.style.marginLeft = "0"; // Move o conteúdo para a esquerda
        } else {
            sidebar.style.left = "0"; // Abre a barra lateral
            content.style.marginLeft = "220px"; // Move o conteúdo para a direita
        }
    }

window.onclick = function(event) {
    var sidebar = document.getElementById("sidebar");
    var content = document.getElementById("content");
    if (event.target != sidebar && event.target != document.getElementsByClassName('menu-btn')[0]) {
        sidebar.style.left = "-220px";
        content.style.marginLeft = "0";
    }
}
