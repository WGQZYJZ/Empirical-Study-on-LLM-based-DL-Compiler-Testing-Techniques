
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = conv_transpose(x1)
        v2 = v1 + min_value # Error: 'min_value' is not defined as the argument for a call to a torch function.
        v3 = v2 + max_value # Error: 'max_value' is not defined as the argument for a call to a torch function.
        return v3

# Initializing the model with keyword arguments min_value=-5 and max_value=100
m  = Model(min_value=-5, max_value=100)


# Inputs to the model