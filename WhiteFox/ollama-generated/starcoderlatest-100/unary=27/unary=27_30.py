
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0., max_value=None):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1, min_value, None)
        v3 = torch.clamp(v2, None, max_value)
        return v3

# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(1, 3, 64, 64)
