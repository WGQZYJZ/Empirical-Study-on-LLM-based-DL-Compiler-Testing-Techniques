
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, t2):
        v3 = torch.cumsum(t2, 1)
        return v3
 
 # Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(4, 64, 64)
