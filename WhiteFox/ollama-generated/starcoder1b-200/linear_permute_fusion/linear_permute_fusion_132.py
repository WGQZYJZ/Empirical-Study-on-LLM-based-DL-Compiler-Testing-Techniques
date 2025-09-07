
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)


# Initializing the model
m = Model()


