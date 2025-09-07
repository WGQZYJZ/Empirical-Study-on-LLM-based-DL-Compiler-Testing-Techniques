
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v2  = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        return v2.permute(-1, -2)


# Initializing the model