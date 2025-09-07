
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
other_tensor = torch.randn(8, 64, 50)
x1 = torch.randn(1, 3, 74, 74)
