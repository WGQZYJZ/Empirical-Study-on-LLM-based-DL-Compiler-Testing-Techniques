
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other_tensor is not None:
            # Initialize the weights of the pointwise convolution so that it uses "other"
            # as its bias.
            self.conv.weight = torch.randn(*self.conv.weight.shape)
 
    def forward(self, x):
        v1 = self.conv(x)
        if isinstance(self.conv, torch.nn.Conv2d):
            other_tensor = None
 
        return (v1 + other_tensor).clamp(min=-3, max=3)


# Initialization of the model with "other" tensor
m  = Model(other_tensor=torch.randn(8, 1))


# Inputs to the model
x1 = torch.randn(2048, 64, 1, 1)
