
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias), 0.1)
        return v2


# Initializing the model
m = Model()
m.fallback_random = False # Enable fallback to random_like
__output = m(x1)

