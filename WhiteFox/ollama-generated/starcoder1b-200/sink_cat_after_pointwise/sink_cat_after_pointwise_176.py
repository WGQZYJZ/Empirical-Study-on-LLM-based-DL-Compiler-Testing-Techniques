
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2 = torch.cat([v1, x2], dim=3)
        return self.linear(t2=v3)


# Initializing the model
m = Model()
