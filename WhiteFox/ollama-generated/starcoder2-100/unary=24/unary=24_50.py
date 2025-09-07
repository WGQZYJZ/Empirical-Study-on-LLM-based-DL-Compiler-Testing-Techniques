
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15748032):
        super().__init__()
        self.conv = torch.nn.Conv2d(
            3, 96, kernel_size=3, padding="same", stride=(2, 2)
            )
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(
    1, 3, 
    560, 589
    )
 
__output__  = m(x1)
