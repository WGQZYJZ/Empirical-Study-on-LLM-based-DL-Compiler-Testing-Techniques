
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1.clamp_min_(50.)
        v3  = v2.clamp_max_(90.)
        return v3


# Initializing the model
m  = Model(50., 90.)

# Inputs to the model<|end_of_code|>
x1  = torch.randn(8, 3, 4, 4)
__output__  = m(x1)

The output is clamped in the following manner. In this example, 50 and 90 are used as the minimum and maximum values of clamping.

v2  = v1.clamp_min_(50.)
v3  = v2.clamp_max_(90.)

