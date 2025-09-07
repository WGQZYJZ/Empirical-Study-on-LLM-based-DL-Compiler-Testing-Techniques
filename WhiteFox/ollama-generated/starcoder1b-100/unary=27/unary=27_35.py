
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 + kwargs['min_value'] # Add the value of min_value to the output of the previous operation
        v3 = v2 / kwargs['max_value']  # Divide the output of the clamped maximum by max_value to get a number in [0, 1]
        return v3


# Initializing the model
m = Model(min_value=0.4965808795222666)
x1 = torch.randn(1, 3, 64, 64) # inputs to the model
