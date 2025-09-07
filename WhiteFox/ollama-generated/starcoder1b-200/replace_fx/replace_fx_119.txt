
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.2)  # Apply dropout to the input tensor
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)


# Initializing the model
m = Model()


# Inputs to the model
__input__ = torch.randn(1, 2, 2)
