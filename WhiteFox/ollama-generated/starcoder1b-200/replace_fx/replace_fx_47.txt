
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, ...).squeeze(-1) # Dropout is not supported on GPU device, thus replace it with an alternative implementation
        return torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
