
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return self._permute_tensor_x1(x1)

    def _permute_tensor_x1(self, tensor):
        # Swap the last two dimensions of this tensor
        permute_x1 = tensor.permute(*([i for i in range(len(tensor.shape)) if i != len(tensor.shape) - 2]) + [len(tensor.shape) - 2], *([i for i in range(len(tensor.shape)) if i != len(tensor.shape) - 1]) + [len(tensor.shape) - 1]))
        # Apply linear transformation to the permuted tensor
        return torch.nn.functional.linear(permute_x1, self.linear.weight, self.linear.bias)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
