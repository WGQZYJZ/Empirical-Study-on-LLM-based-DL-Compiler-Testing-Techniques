
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor = None):
        super().__init__()
        if not other_tensor is None:
            self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if not other_tensor is None:
            v2 = v1 - other_tensor
        else:
            v2 = v1 - 0.5
        return v2

# Initializing the model with the second pattern
m = Model(torch.rand(8))

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
