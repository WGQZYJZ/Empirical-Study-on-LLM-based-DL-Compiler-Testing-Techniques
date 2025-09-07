
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        k1, k2 = self.conv(x1), self.conv(x2)
        return (k1 * k2).sum(-1)


# Initializing the model
m = Model()


# Inputs to the model
q  = torch.randn(2, 3, 64, 64)
k1 = torch.randn(2, 8, 32, 32)
x1 = torch.randn(1, 3, 64, 64)


# Computing the dot product of the inputs with query and key tensor
