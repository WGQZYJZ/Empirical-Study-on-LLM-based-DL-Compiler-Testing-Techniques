
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.permute(x1, [0, 2, 1]) # Swaps the first and last two dimensions of x1
        v2 = torch.nn.functional.linear(v1, self.linear.weight)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
