
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other
        return v2


# Initializing the model and passing another tensor as a keyword argument to the addition operation when initializing it
m  = Model(torch.randn(3))

 # Inputs to the model (input_tensor is unchanged here from previous example)
x1 = torch.randn(1, 3, 64, 64)
 
 