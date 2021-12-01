const dateInput = document.getElementById('id_vitals_date')

const picker = MCDatepicker.create({
    el: '#id_vitals_date',
    dateFormat: 'yyyy-mm-dd',
    closeOnBlur: true,
    selectedDate: new Date(),
})

dateInput.addEventListener("click", (evt) => {
picker.open()
})