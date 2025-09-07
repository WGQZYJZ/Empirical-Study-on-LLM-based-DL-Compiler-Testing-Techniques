
class Model(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_dim, output_dim, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.mm(v1, v1)
        t2 = torch.cat([t1, t1])
        return t2


# Initializing the model
m = Model(3, 8)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
