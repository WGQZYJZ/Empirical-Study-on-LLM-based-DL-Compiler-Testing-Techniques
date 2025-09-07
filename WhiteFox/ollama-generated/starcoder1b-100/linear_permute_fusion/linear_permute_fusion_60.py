
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = x1.permute(0, 2, 1)
        return torch.cat((v1, v2), dim=-1)


# Initializing the model
m = Model()
