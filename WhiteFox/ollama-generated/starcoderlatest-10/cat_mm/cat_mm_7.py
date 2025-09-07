
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 32, 1, stride=2, padding=0)
 
    def forward(self, x):
        v1 = torch.mm(x[::2], x[1::2])
        t2 = torch.cat([v1] * (len(x) // 4), dim=2)
        return self.conv(t2)


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(16, 16)
