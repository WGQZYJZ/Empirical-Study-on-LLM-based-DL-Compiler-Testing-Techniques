
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, inp=1.0):
        v1 = self.conv(x1) * inp  # The 'inp' tensor is passed as a keyword argument
        return v1


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(1, 8, 64, 64)
