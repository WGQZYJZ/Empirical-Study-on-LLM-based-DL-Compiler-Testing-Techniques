
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1])
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(3, 4) # The size of tensor `x1` is (3, 4).
x2  = torch.randn(6, 7) # The size of tensor `x2` is (6, 7).
