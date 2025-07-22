const inputValue = document.querySelector('#inputValue');
    addBtn = document.querySelector("#add_btn");
    removeBtn = document.querySelector("#remove_btn");


addBtn.addEventListener("click", (event) => {
    console.log(inputValue.value);
    if (inputValue.value != 0) {
        inputValue.value = parseInt(inputValue.value) - 1;
    }
})

removeBtn.addEventListener("click", (event) => {
    console.log(inputValue.value);
    inputValue.value = parseInt(inputValue.value) + 1;
})