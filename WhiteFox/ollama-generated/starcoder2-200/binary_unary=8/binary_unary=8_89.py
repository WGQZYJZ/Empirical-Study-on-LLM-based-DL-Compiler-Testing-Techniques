
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn(803495)
        v1  = self.conv(x1)
        v6  = v2 + v1 
        return torch.relu(v6)

# Initializing the model
m  = Model()

 # Inputs to the model
 x1   = torch.randn(803495, 3, 64, 64)
 
