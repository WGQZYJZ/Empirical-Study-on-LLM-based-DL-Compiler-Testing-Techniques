
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        v1 = x1.permute(0, 2, 1)
        if x2 is not None:
            v2 = torch.cat([v1, x2], dim=2).view(-1, 4)
        else:
            v2 = v1

        return torch.relu(torch.matmul(v2, self.linear.weight))


# Initializing the model
m = Model()


