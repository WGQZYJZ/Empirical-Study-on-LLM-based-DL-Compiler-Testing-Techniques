
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.bmm(v1, x2.permute(0, 2, 1))
        return torch.matmul(x2, self.linear2.weight), torch.matmul(v1, self.linear1.weight)


# Initializing the model
m = Model()


