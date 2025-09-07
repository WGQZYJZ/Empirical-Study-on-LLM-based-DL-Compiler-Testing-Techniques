
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return torch.clamp(x2 + 3) / 6
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(80, 96, 57, 41)

 