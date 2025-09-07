
class Model(torch.nn.Module):
    def __init__(self, min_value=-10, max_value=40):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*8, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 32*32*8))
        v2  = torch.clamp_min(v1, min_value=min_value) # clamping value
        v3  = torch.clamp_max(v2, max_value=max_value) # clamping value
        return v3
# Initializing the model with a minimum and maximum value of -50 and 90 respectively:
m = Model(-50., 90.)


# Inputs to the model. 
x1 = torch.randn(2, 32*32*8) # Input size is different.
