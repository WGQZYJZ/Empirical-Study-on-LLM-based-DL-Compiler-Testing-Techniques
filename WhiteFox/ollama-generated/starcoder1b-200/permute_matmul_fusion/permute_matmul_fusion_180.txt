
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 4)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)  # x1 -> (x1, x1, ... x2, x2)
        t2 = self.linear(t1)  # Apply linear transformation to the permuted tensors.
        return torch.cat([t1, t2], dim=1)


# Initializing the model
m = Model()

