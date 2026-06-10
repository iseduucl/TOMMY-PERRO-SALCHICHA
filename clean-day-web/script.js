// Verifica que JavaScript está conectado
console.log("Página Clean Day cargada correctamente");

// Año automático en el footer
const anio = document.getElementById("anio");

if (anio) {
    anio.textContent = new Date().getFullYear();
}

// Mini chatbot Clean Day
const abrirChat = document.getElementById("abrirChat");
const cerrarChat = document.getElementById("cerrarChat");
const chatVentana = document.getElementById("chatVentana");

if (abrirChat && cerrarChat && chatVentana) {
    abrirChat.addEventListener("click", () => {
        chatVentana.classList.toggle("activo");
    });

    cerrarChat.addEventListener("click", () => {
        chatVentana.classList.remove("activo");
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            chatVentana.classList.remove("activo");
        }
    });
}
