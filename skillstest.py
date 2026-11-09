from pyscript import document, when

@when("click", "#search-btn")
def search_element(event):
    input_element = document.querySelector("#symbol-input")
    symbol = input_element.value.strip()
    lookup_key = symbol.lower()
    output_div = document.querySelector("#result-output")
    
    elements = {
        "h": ("H", "Hydrogen", "1", "1.008"),
        "he": ("He", "Helium", "2", "4.003"),
        "c": ("C", "Carbon", "6", "12.011"),
        "n": ("N", "Nitrogen", "7", "14.007"),
        "o": ("O", "Oxygen", "8", "15.999"),
        "f": ("F", "Fluorine", "9", "18.998"),
        "ne": ("Ne", "Neon", "10", "20.180"),
        "p": ("P", "Phosphorus", "15", "30.974"),
        "s": ("S", "Sulfur", "16", "32.06"),
        "cl": ("Cl", "Chlorine", "17", "35.45"),
        "ar": ("Ar", "Argon", "18", "39.95"),
        "se": ("Se", "Selenium", "34", "78.971"),
        "br": ("Br", "Bromine", "35", "79.994"),
        "kr": ("Kr", "Krypton", "36", "83.88"),
        "i": ("I", "Iodine", "53", "126.90"),
        "xe": ("Xe", "Xenon", "54", "131.29"),
        "rn": ("Rn", "Radon", "86", "222"),
    }
    
    result = elements.get(lookup_key, ["", "", "", ""])

    success_html = f"""
    <div class="card border-primary shadow-sm">
        <div class="card-body">
            <h5 class="card-title text-primary">Result:</h5>
            <p class="mb-1"><strong>Symbol:</strong> {result[0]}</p>
            <p class="mb-1"><strong>Element:</strong> {result[1]}</p>
            <p class="mb-1"><strong>Atomic Number:</strong> {result[2]}</p>
            <p class="mb-0"><strong>Atomic Mass:</strong> {result[3]}</p>
        </div>
    </div>
    """

    error_html = f"""
    <div class="card border-danger shadow-sm">
        <div class="card-body">
            <h5 class="card-title text-danger">Element not found!</h5>
            <p class="mb-0">This symbol "<strong>{symbol}</strong>" does not exist in the non-metals list!</p>
        </div>
    </div>
    """

    html_list = [error_html, success_html]
    has_element = int(lookup_key in elements)
    
    output_div.innerHTML = html_list[has_element]