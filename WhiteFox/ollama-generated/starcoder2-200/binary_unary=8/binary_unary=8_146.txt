
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # <- this is added to another tensor
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
other_tensor = torch.randn(4, 8, 60, 59)

# Inputs to the model
x1 = torch.randn(1, 3, 70, 70)

__output__  = m(x1)

