// (function () {
//     const darkSwitch = document.getElementById("darkSwitch");

//     if (darkSwitch) {

//         initTheme();

//         darkSwitch.addEventListener("click", function () {
//             resetTheme();
//             console.log("click")
//         });
//         function initTheme() {
//             const darkThemeSelected =
//                 localStorage.getItem("darkSwitch") !== null &&
//                 localStorage.getItem("darkSwitch") === "dark";
//             darkSwitch.checked = darkThemeSelected;

//             darkThemeSelected
//                 ? document.body.setAttribute("data-theme", "dark")
//                 : document.body.removeAttribute("data-theme");
//         }
//         function resetTheme() {
//             if (darkSwitch.checked) {
//                 document.body.setAttribute("data-theme", "dark");
//                 localStorage.setItem("darkSwitch", "dark");
//             } else {
//                 document.body.removeAttribute("data-theme");
//                 localStorage.removeItem("darkSwitch");
//             }
//         }
//     }
// })();



darkLight = document.querySelector('#darkSwitch')
darkLight.addEventListener('click', function () {
    if (document.body.getAttribute('data-theme') === 'light') {
        document.body.setAttribute('data-theme', 'dark')
        localStorage.setItem('selected-theme', 'dark');
    } else {
        document.body.setAttribute('data-theme', 'light')
        localStorage.setItem('selected-theme', 'light');
    }

})
if (typeof (Storage) !== 'undefined') {
    if (localStorage.getItem('selected-theme') == 'light') {
        document.body.setAttribute('data-theme', 'light');
    }
    else if (localStorage.getItem('selected-theme') == 'dark') {
        document.body.setAttribute('data-theme', 'dark');
    }
}