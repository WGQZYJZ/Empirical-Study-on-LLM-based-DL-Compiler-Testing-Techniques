
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transposed = torch.nn.ConvTranspose2d(8, 3, 1, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transposed(x1)
        min_value = torch.min(v1).item() # Use the function to get the minimum value of an input tensor
        max_value = torch.max(v1).item() # Use the function to get the maximum value of an input tensor
        v2  = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
