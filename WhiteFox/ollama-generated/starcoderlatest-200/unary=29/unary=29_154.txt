
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=10):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 5, stride=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 576, 464)
