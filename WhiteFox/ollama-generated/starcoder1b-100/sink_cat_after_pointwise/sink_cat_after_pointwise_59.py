
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1  = torch.cat([x1, x1, ...], dim=0)
        v2  = self.linear(t1).permute(2, 3, 0, 1)
        return v2


# Initializing the model
m = Model()


