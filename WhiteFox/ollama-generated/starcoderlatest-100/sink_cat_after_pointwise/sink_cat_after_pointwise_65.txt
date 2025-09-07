
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=-1)  # Concatenate the last two dimensions of the input tensors and reshape it to a tensor with two dimensions.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)  # Apply linear transformation on this reshaped tensor
        return v2


# Input tensors for the model
x1 = torch.randn(1, 3, 5)
x2 = torch.randn(1, 4, 3)
__input_tensor__ = x1
x3 = torch.randn(1, 6, 8)


