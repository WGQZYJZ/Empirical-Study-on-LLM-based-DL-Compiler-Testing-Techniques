
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, x1 + 0.5], dim=0)
        t2 = t1.view(t1.size(0), -1)
        t3 = torch.relu(t2)
        return t3
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 2)
