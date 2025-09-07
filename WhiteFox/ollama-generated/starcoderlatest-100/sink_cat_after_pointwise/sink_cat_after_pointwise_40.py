
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, x2], dim=0)
        v1 = t1.view(t1.size()[0], -1) # Reshape the concatenated tensor
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 4, 2)
