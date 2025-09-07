
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = linear(x1)
        v2  = torch.clamp_min(v1, min=-100.) # min=-100 here to match the original input
        v3  = torch.clamp_max(v2, max=1e5)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 8) + min(-90.) # The input should be modified to match the provided min and max values.
__output__  = m(x1)

