
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
 
        t2 = torch.cumsum(x0, 1)
        return t2
 
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(64, 3, 8, 5).abs().long()
