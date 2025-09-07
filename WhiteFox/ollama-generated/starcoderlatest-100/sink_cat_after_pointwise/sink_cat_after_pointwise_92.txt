
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        t2 = torch.cat([t1, 2 * t1], dim=0)
        t3 = t2.view(-1, 8)
        t4 = torch.relu(t3)
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 6, 5)
