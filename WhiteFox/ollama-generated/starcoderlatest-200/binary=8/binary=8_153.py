
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1, bias=False)
            self.conv.weight.data = other
 
    def forward(self, x1):
        if isinstance(self.conv.bias, torch.Tensor): # If a bias is already there in the conv layer...
            v2 = v1 + self.conv.bias
        else:
            raise Exception("The model does not have a bias")
        return v6


# Initializing the model
m = Model()
m.conv.weight.data = torch.randn(8, 3, 1, 1)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
