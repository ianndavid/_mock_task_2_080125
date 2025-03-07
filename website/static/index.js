
 // Get today's date
const today = new Date();
const yyyy = today.getFullYear();
const mm = String(today.getMonth() + 1).padStart(2, '0'); // Months are zero-based
const dd = String(today.getDate()).padStart(2, '0');
// Format today's date as YYYY-MM-DD
 const todayFormatted = `${yyyy}-${mm}-${dd}`;
                      
 // Calculate the date 5 days from today
const maxDate = new Date(today);
maxDate.setDate(maxDate.getDate() + 400);
const maxYyyy = maxDate.getFullYear();
const maxMm = String(maxDate.getMonth() + 1).padStart(2, '0');
const maxDd = String(maxDate.getDate()).padStart(2, '0');
const maxDateFormatted = `${maxYyyy}-${maxMm}-${maxDd}`;
                      
                              // Set the min and max attributes for the date input
const dateInput = document.getElementById('Hotel_Check_in');
dateInput.setAttribute('min', todayFormatted);
dateInput.setAttribute('max', maxDateFormatted);

const dateInput2 = document.getElementById('Hotel_Check_Out');
dateInput2.setAttribute('min', todayFormatted);
dateInput2.setAttribute('max', maxDateFormatted);

                               


function changeFont() {
    const changefnt = document.querySelectorAll("*");

    changefnt.forEach(element => {
        element.style.fontStyle = "italic";
        element.style.fontWeight = "bold";
        element.style.fontSize = "20px";
        element.style.fontFamily = "Arial, serif";
    });

    // Save the font change state
    localStorage.setItem("changefnt", "true");
}
