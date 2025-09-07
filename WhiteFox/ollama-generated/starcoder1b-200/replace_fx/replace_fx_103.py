
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias), ...) # Apply dropout to the input tensor
        return v2


# Initializing the model
m = Model()
m.apply_fallback_random = True


# Inputs to the model
x1 = torch.randn(1, 2, 2)
