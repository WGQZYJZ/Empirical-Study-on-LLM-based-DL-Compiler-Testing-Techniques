
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = torch.randn(3).view(-1, 3, 56, 56)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - self.other
        v3 = F.relu(v2)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model