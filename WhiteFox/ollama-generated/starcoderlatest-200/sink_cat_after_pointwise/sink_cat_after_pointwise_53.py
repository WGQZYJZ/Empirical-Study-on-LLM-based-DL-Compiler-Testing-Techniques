
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        t3 = torch.cat([t1, t2], dim=-1)
        t4 = t3.view(t3.shape[0], -1)
        return torch.relu(t4)


# Inputs to the model
t1  = torch.randn(1, 10)
t2  = torch.randn(1, 16)
