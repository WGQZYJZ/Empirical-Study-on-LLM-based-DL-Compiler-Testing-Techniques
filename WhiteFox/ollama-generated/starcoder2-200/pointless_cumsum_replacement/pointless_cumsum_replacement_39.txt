
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, v6):
        return torch.cumsum(v6 + 10, 1)
    
# Initializing the model
m = Model()

 # Inputs to the model
v5_1 = torch.randn(429, 737, dtype=torch.float64)
v5_2 = m(v5_1)
