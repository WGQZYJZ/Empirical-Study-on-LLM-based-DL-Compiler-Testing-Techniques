
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = v1 * min_value # Clamp to a minimum value provided as keyword argument
        v3  = v2 * max_value # Clamp the previous output to a maximum value provided as keyword argument
        return v3


# Initializing the model with keyword arguments for the clamping values:
m = Model(max_value=0.75, min_value=-1)

# Inputs to the model with a custom clamping minimum and maximum value of -2 and 4 respectively<|end_of_input|>:
__output__  = m(torch.randn(1, 3, 64, 64))

