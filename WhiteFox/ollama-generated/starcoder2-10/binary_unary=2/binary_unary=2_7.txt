
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - torch.randn()
        v3  = F.relu(v2) 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
__input_1__ = torch.randn(1, 3, 64, 64)

__output___  = m(__input_1__)

