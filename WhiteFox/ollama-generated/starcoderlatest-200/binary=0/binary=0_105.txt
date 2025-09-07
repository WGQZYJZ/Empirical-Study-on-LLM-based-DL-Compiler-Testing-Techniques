
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model and inputs
m = Model()
input_tensor = torch.randn(1, 3, 64, 64)


# Creating a second tensor which is going to be added to x1
t1 = torch.rand((1, 8, 64, 64))
other = t1 * 0.5
input_dict = {"x1": input_tensor, "other": other}


# Forward pass of the model with the two tensors as inputs and the additional arguments
