
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v7 = torch.full([4096], 3) + 5
        return v7

 # Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
