
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_a = torch.nn.Linear(2, 2)
        self.linear_b = torch.nn.Linear(3, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        return self.linear_a(v1) * self.linear_b(v2)

# Initializing the model
m = Model()


