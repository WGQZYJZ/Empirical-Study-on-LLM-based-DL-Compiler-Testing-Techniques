
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_a = torch.nn.Linear(2, 2)
        self.linear_b = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, self.linear_a(x2))
        v3 = torch.bmm(v2, self.linear_b(x1))
        return v3


# Initializing the model
m = Model()


