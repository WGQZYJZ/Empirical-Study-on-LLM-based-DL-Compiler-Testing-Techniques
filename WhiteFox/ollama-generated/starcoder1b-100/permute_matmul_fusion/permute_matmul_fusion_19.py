
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.bmm(v1, x2)  # or torch.matmul(v1, x2)
        return self.linear1(v2), self.linear2(v2)


# Initializing the model
m = Model()


