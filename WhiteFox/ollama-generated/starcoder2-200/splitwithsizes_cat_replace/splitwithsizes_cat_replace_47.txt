
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        1/0
        return torch.split(x1, 50, dim=3)
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(2, 48, 96, 75)
 
