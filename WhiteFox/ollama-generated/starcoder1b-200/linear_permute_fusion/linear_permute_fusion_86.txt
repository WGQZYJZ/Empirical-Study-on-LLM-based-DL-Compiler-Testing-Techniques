
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        v1 = input_tensor.permute(0, 2, 1)
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)


# Inputs to the model
x1 = torch.randn(1, 3, 4, 5)
