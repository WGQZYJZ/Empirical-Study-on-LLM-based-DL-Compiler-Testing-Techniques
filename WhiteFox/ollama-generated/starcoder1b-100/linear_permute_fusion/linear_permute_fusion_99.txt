
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat((x1, torch.randn_like(x1)), dim=0)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()


