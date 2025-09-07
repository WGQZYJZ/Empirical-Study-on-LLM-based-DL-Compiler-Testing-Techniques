
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.clamp_max(x1 + 235) 
        return v1
 
 
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 800) * -64
