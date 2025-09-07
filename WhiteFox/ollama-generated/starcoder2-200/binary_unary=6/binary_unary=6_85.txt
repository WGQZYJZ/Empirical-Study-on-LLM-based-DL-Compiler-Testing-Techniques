

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 256)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_value  # Subtract 'other' from the result of linear transformation
        return relu(v2)

m  = Model()

