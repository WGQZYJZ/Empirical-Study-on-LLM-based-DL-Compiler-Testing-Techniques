
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = other  # another tensor
        v3  = self.conv(x1) + v2 
        v4  = torch.relu(v3)
        return v4
 
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
 
