
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        t1 = torch.cat([v1[:, :, :4], v1[:, :, 4:]], dim=2)
        v2 = torch.relu(t1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 4)
