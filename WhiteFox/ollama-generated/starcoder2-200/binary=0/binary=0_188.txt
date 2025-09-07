
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other = torch.nn.Parameter(torch.rand_like(other)) if other is not None else 1

    def forward(self, x):
        v1  = self.conv(x)
        return v1 + self.other


# Initializing the model
m = Model()
m2 = Model(other=m.conv.weight)

# Inputs to the model
x   = torch.randn(32, 3, 64, 64)
x2  = m2(x)

m(torch.rand(10))  # Randomized input tensor for previous call of model to generate a random model