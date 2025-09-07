
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, x2], dim=...)
        t2 = t1.view(...)
        t3 = torch.relu(t2)

# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(2, 2)
x2 = torch.randn(2, 4)
