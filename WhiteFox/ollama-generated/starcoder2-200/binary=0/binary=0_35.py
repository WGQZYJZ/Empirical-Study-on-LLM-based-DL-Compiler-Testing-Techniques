
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        return self.conv(x) + 5


# Initializing the model with `other` tensor passed as a keyword argument to convolution operation:
m  = Model()
m.conv.weight = torch.nn.Parameter(torch.tensor([[1., 0], [0, -1]]), requires_grad=True)

 # Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
  __output__  = m(x1)
