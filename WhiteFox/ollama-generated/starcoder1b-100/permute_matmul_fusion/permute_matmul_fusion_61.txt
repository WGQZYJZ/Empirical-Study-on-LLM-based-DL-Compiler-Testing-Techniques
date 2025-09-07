
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.BMM
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2).transpose(-1, -2)
        return torch.bmm(torch.matmul(x1, x2), torch.relu(self.linear1(v2)))


# Initializing the model
m = Model()


