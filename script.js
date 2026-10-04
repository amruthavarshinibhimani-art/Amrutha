document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const button =
                form.querySelector("button");

            button.innerText =
                "Generating AI Event Plan...";

            button.disabled = true;

        });

    }

});