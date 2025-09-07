
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=-0.957343633990935) # Apply the clamp minimum function to the output of the convolution and provide a negative value for the minimum value as an argument
        v3 = torch.clamp_max(v2, max_value=1.85153381187439)  # Apply the clamp maximum function to the output of the previous operation and provide a positive value for the maximum value as an argument
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
