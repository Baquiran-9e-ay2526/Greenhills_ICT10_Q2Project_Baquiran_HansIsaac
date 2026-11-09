from pyscript import document, when

@when("click", "#greet-btn")
def show_greeting(event):
    output_div = document.querySelector("#pyscript-output")
    output_div.innerHTML = "Thank you for meeting me on my page! And always remember to pursue your dreams forever, and never surrender."