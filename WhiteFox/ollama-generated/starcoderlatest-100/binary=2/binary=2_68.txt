
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v6


# Initializing the model
other_tensor = torch.randn(4, 3, 5, 8).requires_grad_() # tensor with requires_grad set to True
m = Model(other_tensor)


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
