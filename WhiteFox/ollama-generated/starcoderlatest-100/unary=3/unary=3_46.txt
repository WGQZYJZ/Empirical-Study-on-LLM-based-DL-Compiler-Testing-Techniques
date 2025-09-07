
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v6  = (0.5 * torch.pow(x1 + 1.0))
        return v6

 # Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 