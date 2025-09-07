
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2) 
        return v3


# Initializing the model
m = Model()
other_tensor  = torch.randn(8, 50) # Any 4D tensor is OK (e.g., 3x64x64)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

