
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model and passing `other` as a keyword argument to the constructor of the model
m = Model(other=torch.tensor([3])) # Passing 3 as an input tensor to `other`, which is added to the output of the convolution

# Inputs to the model