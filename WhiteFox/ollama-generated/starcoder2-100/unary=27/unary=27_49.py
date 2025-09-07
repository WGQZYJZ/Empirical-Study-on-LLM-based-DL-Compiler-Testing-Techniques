
class Model(torch.nn.Module):
    def __init__(self, max_value=100000.0, min_value=-100000.0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=0) 
        v3  = torch.clamp_max(v2, max_value=99999.56784)
        return v3

# Initializing the model with minimum and maximum values
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

