
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
other  = torch.randn(3, 8, 64, 64) # Randomly generated 8 channel tensor with shape [1x64x64]
__output__  = m(x1)

