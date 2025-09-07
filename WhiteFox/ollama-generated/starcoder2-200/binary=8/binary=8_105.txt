
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 0 # Adding another tensor that will be provided by the user
        return v2


# Initializing the model and defining a tensor to provide as a keyword argument in the addition operation
t3  = torch.randn((5,4)) # A random tensor of shape (5,4) is generated. This can be replaced with another tensor that will be passed by the user.
m  = Model()


# Inputs to the model and addition of other_tensor during runtime. The "other" keyword argument is provided as a torch Tensor in this example.
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1, other=t3)

