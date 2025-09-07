
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2, t3):
        v1 = torch.cat([t1, t2], dim=0)
        v2 = v1.view(-1, 4, 2)
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
t1 = torch.randn(1, 8, 4, 2)
t2 = torch.randn(1, 4, 2)
