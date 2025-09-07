
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.randn(24)
        v2  = torch.clamp_min(v1, -10**50) 
        v3  = torch.clamp_max(v2, 10**50)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(24)

