
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(1, 128, 16, 16)
k = torch.randn(1, 128, 16, 16)
v = torch.randn(1, 8, 32, 32)


