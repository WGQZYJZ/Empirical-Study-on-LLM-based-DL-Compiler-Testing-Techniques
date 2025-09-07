
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.randn(8) # Randomly generate an 8-element tensor
        v2 = self.conv(v1 + other) 
        return v2
 
# Initializing the model