
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
 
        # This is where the model differs from the previous one
        v2  = v1 + other_tensor
        
        v3 = torch.relu(v2)

        return v3


# Initializing the model with random tensors:
m, other_tensor   = Model(), torch.randn(4, 8, 64, 64)

# Inputs to the model:
x1  = torch.randn(1, 3, 64, 64)
__output__     = m(x1)

