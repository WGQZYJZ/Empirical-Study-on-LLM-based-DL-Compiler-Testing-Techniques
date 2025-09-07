
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value=0.)
        return torch.clamp_max(v2, max_value=4.)


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(3, 8, 65, 97)
__output__  = m(x1)
