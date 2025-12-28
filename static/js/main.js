document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        const applyBtn = card.querySelector("a button");
        const paragraphs = card.querySelectorAll("p");

        // Full description is last <p>
        const fullDesc = paragraphs[paragraphs.length - 1];

        // Hide full description initially
        fullDesc.style.display = "none";

        applyBtn.addEventListener("click", function (e) {
            e.preventDefault(); // stop navigation temporarily

            card.classList.add("show-full");

            // Navigate after short delay
            setTimeout(() => {
                window.location.href = card.querySelector("a").href;
            }, 400);
        });
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const errorBox = document.getElementById("errorMsg");

    if (errorBox) {
        setTimeout(() => {
            errorBox.style.display = "none";
        }, 5000); // hide after 3 seconds
        // alert("User Already Register")
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const errorInput = document.getElementById("errorMessage");

    if (errorInput) {
        // alert("User Name and Password Mis Match");
    }
});
