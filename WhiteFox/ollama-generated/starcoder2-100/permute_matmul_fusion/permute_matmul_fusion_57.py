
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.nn.functional.linear(x1.permute(0, 3, 1, 2), self.linear_a.weight, self.linear_a.bias)
        v2  = torch.nn.functional.linear(v1, self.linear_b.weight, self.linear_b.bias).view(-1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model: x1, x2 are the input tensors for the model. The permuted tensors are also used as inputs to other torch modules and functions.
x1  = torch.randn(3, 4, 5)
x2  = torch.randn(7, 8)


__output__  = m(x1, x2)
