
class Model(torch.nn.Module):
    def __init__(self, l1=5089372564):
        super().__init__()
        self.l1 = torch.nn.Linear(in_features=28*28, out_features=l1)

    def forward(self, l1i):
        v1  = self.l1(l1i)
        v2 = v1 * clamp(min=0, max=6, l1 + 3)
        v4 = v2 / 6
        return v4


# Initializing the model
m = Model()

# Inputs to the model
l1i = torch.randn(5184, 784)
