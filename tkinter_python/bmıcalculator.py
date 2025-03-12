import tkinter

# Function to determine BMI category (BMI kategorisini belirleyen fonksiyon)
def write_result(bmi):
    result_string = f"Your BMI is: {round(bmi, 2)}. You are "
    
    if bmi <= 16:
        result_string += "severely thin!"  # (Aşırı zayıf)
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"  # (Orta derecede zayıf)
    elif 17 < bmi <= 18.5:
        result_string += "mildly thin!"  # (Hafif zayıf)
    elif 18.5 < bmi <= 25:
        result_string += "normal!"  # (Normal)
    elif 25 < bmi <= 30:
        result_string += "overweight!"  # (Fazla kilolu)
    elif 30 < bmi <= 35:
        result_string += "obese (Class I)!"  # (Obez - Sınıf 1)
    else:
        result_string += "obese (Class III)!"  # (Aşırı obez - Sınıf 3)
    
    return result_string

# Function to calculate BMI (BMI hesaplama fonksiyonu)
def calculator_bmi():
    height = height_input.get()  # Get the height input (Boy girişini al)
    weight = weight_input.get()  # Get the weight input (Kilo girişini al)

    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height:")  # (Hem kilo hem boy girin)
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2  # BMI formula (BMI formülü)
            result_string = write_result(bmi)  # Determine BMI category (BMI kategorisini belirle)
            result_label.config(text=result_string)  # Display result (Sonucu göster)
        except ValueError:
            result_label.config(text="Enter a valid number!")  # (Geçerli bir sayı girin!)

# Create main window (Ana pencereyi oluştur)
window = tkinter.Tk()
window.title("BMI Calculator")  # (BMI Hesaplayıcı)
window.config(padx=35, pady=35)  # (Kenarlardan boşluk bırak)

# Weight input section (Kilo giriş bölümü)
weight_input_label = tkinter.Label(text="Enter your weight (kg):")  # (Kilonuzu girin (kg))
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)  # (Kilo giriş kutusu)
weight_input.pack()

# Height input section (Boy giriş bölümü)
height_input_label = tkinter.Label(text="Enter your height (cm):")  # (Boyunuzu girin (cm))
height_input_label.pack()

height_input = tkinter.Entry(width=10)  # (Boy giriş kutusu)
height_input.pack()

# Calculate button (Hesapla butonu)
calculator_button = tkinter.Button(text="Calculate", command=calculator_bmi)  # (Hesapla butonu ve fonksiyon bağlantısı)
calculator_button.pack()

# Result label (Sonuç etiketi)
result_label = tkinter.Label()  # (Sonucun gösterileceği yer)
result_label.pack()

# Run the window loop (Pencere döngüsünü başlat)
window.mainloop()