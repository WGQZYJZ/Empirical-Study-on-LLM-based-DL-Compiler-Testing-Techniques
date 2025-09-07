
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, t2=None):
        v1  = x1.permute(0, 2, 1)
        if t2 is not None:
            return torch.relu(torch.matmul(v1, self.linear.weight))
        else:
            return torch.relu(torch.matmul(v1, self.linear.weight))


# Initializing the model
m = Model()

