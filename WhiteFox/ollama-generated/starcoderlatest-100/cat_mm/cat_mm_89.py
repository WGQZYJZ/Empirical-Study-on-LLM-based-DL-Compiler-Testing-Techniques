
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.m1(x1)
        # concatenate along dimension of input tensor
        v2 = torch.cat([v1, v1], dim=1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
