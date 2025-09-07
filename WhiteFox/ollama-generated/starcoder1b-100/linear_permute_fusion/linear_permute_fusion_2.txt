
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight)  # Linear function with the same weights and bias as `m`
        v2 = x1.permute(0, 2, 1).contiguous()  # Permute the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
