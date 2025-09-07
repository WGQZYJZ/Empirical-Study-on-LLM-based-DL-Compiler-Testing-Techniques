
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0 = torch.ones_like(x1[:, :, 5:64-5:,:64-5:]) # Create a 3D tensor of shape (batch size, number of channels, height, width), which is filled with ones. 
        v1  = self.conv(x1)
        v2  = v0 + v1
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
