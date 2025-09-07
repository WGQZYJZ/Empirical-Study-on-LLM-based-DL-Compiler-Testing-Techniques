
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = nn.Parameter(torch.tensor([1.0]), requires_grad=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, self.scale_factor.view(-1, 1, 1))
        v3 = v2 + 1
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
