
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, x2):
        v4 = torch.cat([t1, x2], dim=1)
        return v4
 
 # Initializing the model
m = Model()

 # Inputs to the model
t1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 3, 64, 64)
