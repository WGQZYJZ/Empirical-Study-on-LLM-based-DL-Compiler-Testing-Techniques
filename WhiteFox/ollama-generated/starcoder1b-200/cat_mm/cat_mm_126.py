
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(1, 3)
        self.m2 = torch.nn.Linear(3, 6)

    def forward(self, x1, x2):
        m1 = self.m1(x1)
        m2 = self.m2(torch.cat([x1, x1, ..., x1], dim=0)) # Concatenation of two input tensors along a certain dimension
        return torch.mm(m1, m2)


# Initializing the model
m = Model()


