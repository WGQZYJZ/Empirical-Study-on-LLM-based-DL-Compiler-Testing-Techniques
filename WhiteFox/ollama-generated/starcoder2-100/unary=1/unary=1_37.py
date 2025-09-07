
m = torch.nn.Linear(28  *  64 + 70, 35)

 # Initializing the model
m  = m()

 # Inputs to the model
x1  = torch.randn(1, 28  *  64 + 70)
 
# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(28  *  64 + 70, 35)

    def forward(self, x1):
         v1 = self.conv(x1)
         v2 = v1  *  (v1  +  ((- 1)**((v1  -  (- 90)))) /  ((v1  -  (- 90))**3))   # Calculation here
         return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 28  *  64 + 70)
 
__output__  = m(x1)

