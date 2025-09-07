
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25) -> None:
        super().__init__()
        self.negative_slope = negative_slope
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 > 0
        v3  = v1 * -self.negative_slope
        v4  = torch.where(v2, v1, v3) # Where is the correct one?
        return v4


# Initializing the model with a negative slope of `-0.5`
model = Model(-0.5)


# Inputs to the model
x_test = torch.randn(8, 3, 64, 64)
__output__  = model(x_test)

