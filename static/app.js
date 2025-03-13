document.addEventListener("DOMContentLoaded", function () {
    const forms = {
        addUserForm: "/adduser",
        addPinForm: "/insertpin",
        addBoardForm: "/insertboard"
    };

    Object.keys(forms).forEach(formId => {
        const formElement = document.querySelector(`#${formId}`);
        if (formElement) {
            formElement.addEventListener("submit", function (e) {
                e.preventDefault();
                fetch(forms[formId], {
                    method: "POST",
                    body: new FormData(this),
                })
                .then(response => response.text())
                .then(data => alert(data))
                .catch(error => console.error("Error:", error));
            });
        }
    });
});
