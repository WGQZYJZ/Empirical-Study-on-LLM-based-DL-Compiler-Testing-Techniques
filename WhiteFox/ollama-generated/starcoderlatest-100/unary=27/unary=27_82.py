
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        min_value = float("-inf") # Minimum value clamping the output of the convolution
        max_value = 0.7293556744131539   # Maximum value clamping the output of the previous operation
        v2 = torch.clamp(v1, min_value=min_value, max_value=max_value)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
