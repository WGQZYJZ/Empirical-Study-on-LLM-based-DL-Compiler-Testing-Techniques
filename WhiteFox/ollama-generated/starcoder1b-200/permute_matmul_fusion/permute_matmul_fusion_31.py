
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_a = torch.nn.Linear(2, 2)
        self.linear_b = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear_a(v1)
        v3 = self.linear_b(x2.permute(0, 2, 1))
        return v2 + v3


# Initializing the model
m = Model()

