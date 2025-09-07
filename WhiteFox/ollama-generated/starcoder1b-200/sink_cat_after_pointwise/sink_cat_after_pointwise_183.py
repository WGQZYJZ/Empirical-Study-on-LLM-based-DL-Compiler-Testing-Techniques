
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        t1  = x1.permute(0, 2, 1)
        t2  = torch.cat([t1, t1], dim=1).view(-1, 8, 4, 4)
        return self.linear(t3)


# Initializing the model
m = Model()


