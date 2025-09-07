
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 15)

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v2.permute(0, 2, 1)


# Initializing the model