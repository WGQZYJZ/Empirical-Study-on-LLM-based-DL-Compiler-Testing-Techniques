
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t2):
        v3 = torch.cumsum(t2, 1)
        return v3
 
 # Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 