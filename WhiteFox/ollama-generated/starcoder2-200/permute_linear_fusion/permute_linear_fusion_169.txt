
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3  = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)

        return v3


# Initializing the model