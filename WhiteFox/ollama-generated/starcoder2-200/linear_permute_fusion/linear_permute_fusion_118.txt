
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x2):
        v3 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        return v3

# Initializing the model