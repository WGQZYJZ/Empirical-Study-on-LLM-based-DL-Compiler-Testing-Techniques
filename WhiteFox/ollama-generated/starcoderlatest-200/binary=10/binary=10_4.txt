
class Model(torch.nn.Module):
    def __init__(self, other_tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if (other_tensor is not None):
            self.linear = torch.nn.Linear(3*64*64, 512)
            self.fc2 = torch.nn.Linear(512, 64*64)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
v2 = m(x1, x1+1)


