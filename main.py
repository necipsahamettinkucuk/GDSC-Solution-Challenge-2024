import Camera
import AI
import torch

print(t.__version__)

print(torch.cuda.is_available())

if torch.cuda.is_available():
    print("Cuda is Availabe")
else:
    print("Cuda Can't be found")
print(torch.version.cuda)

c = Camera.Cam()

# Colab'da eğittimiz ağırlık
ai = AI.Model("best.pt")

c.read_with_ai(ai)