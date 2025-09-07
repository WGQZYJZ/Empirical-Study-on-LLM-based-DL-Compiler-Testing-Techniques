
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1, x2], dim=1)
        return v6
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
