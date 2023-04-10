function togglePasswordVisibility() {
    var passwordField = document.getElementById("password-input");
    var visibilityButton = document.getElementById("visibility-button");
    
    if (passwordField.type === "password") {
      passwordField.type = "text";
      visibilityButton.textContent = "Hide";
    } else {
      passwordField.type = "password";
      visibilityButton.textContent = "Show";
    }
}  