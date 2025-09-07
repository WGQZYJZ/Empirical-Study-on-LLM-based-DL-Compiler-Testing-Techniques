
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.clamp_(min_value=min_value)
        v3 = v2.clamp_(max_value=max_value)
        return v3


# Initializing the model
m = Model(min_value=-0.5, max_value=1.5)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
