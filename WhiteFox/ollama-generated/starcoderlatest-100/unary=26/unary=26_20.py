
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model and set its parameters to be tunable
m = Model(negative_slope=1.5798228770675544e-06)
set_hyperparams(m)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
