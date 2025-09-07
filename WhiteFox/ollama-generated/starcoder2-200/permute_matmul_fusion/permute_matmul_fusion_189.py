
class Model(torch.nn.Module):
    def __init__(self, n, dim=2):
        super().__init__()

        self.linear = torch.nn.Linear(n, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 3, 1, 2) 
        v2 = x2.permute(0, 2, 3, 1)
        v3 = torch.bmm(v1, v2)

        return self.linear(v3)


# Initializing the model
m = Model(4)


# Inputs to the model