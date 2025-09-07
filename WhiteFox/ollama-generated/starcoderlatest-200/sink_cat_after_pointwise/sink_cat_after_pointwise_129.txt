
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        t3 = torch.cat([t1, t2], dim=-1)
        return torch.relu(t3).permute(0, 2, 1)

# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.randn(1, 5)
t2 = torch.randn(1, 7)
