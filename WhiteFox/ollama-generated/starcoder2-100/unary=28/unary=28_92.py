
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=0.7897839657306671) # Minumum value is provided as keyword argument
        v3 = torch.clamp_max(v2, max_value=-0.4148276927471161) # Maximum value is provided as keyword argument
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(256, 1024)
__output__  = m(x1)
