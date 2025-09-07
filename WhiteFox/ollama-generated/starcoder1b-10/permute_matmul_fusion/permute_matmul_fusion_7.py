
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear1(v1)
        return torch.bmm(torch.cat((v1[:, :, :1], v2), dim=-1), x2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4)
x2 = torch.randn(2, 4, 2)
