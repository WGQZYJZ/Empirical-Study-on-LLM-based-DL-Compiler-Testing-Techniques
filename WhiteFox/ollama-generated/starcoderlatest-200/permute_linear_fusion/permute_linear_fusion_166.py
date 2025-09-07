
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.cat((x1, torch.ones_like(x1)), dim=1) # Concatenate the tensor x1 and ones into the third dimension of an input tensor
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 2)
