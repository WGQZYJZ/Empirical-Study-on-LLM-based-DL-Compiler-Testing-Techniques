
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.convtranspose(x1)
        v2 = v1 + 3 
        v3 = torch.clamp_min(v2, 0) # clamped min(x, 6)
        v4 = torch.clamp_max(v3, 6) # clamp max(v4, x) at a minimum of 6 and a maximum of 6; clamp_max returns v4
        v5 = v4 / 6 
        return v5


# Initializing the model: 
m = Model()


# Inputs to the model: 
	- x1 = torch.randn(3, 8, 2) (randomly generated input of size 3x8x2)

 