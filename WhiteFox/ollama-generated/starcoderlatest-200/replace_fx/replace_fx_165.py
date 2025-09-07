 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    # This function contains the invocation of two random functions, one is dropout function, another one is rand_like function. These two functions should not be optimized away.
    def forward(self, x1):
        v1 = torch.nn.functional.dropout(input_tensor, 0.5)
        v2 = torch.rand_like(x1)
        return torch.cat((v1, v2), dim=1)


# Inputs to the model
x1 = torch.randn(1, 8, 4)
