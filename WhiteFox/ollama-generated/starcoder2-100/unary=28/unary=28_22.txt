
class Model(torch.nn.Module):
    def __init__(self, maxval=10.25678943210987):
        super().__init__()
        self.linear  = torch.nn.Linear(in_features=8*8*8, out_features=1)
        self.maxval = maxval
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, -self.maxval) # Clamp the minimum value of the output to a constant `0`
        v3 = torch.clamp_max(v2, +self.maxval)  # Clamp the maximum value of the previous operation to another constant `0`.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4*8*8, 8*8*8)
__output__  = m(x1).sum().item() == 0

