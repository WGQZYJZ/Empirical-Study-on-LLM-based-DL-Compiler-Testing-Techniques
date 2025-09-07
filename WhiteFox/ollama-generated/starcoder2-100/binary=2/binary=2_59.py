
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 - other


# Initializing the model
m = Model()
other = tensor([[[[0]]]]) # A constant tensor of shape [1, 1, 3, 8] and data type `torch.float`


# Inputs to the model
x1  = torch.randn(256, 3, 96, 96)
__output__  = m(x1)

