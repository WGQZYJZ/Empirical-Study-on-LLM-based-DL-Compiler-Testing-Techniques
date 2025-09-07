
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v = torch.tanh(x)
         return v
 
# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(5)
__output__  = m(x)