
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.softmax(x1, dim=-1).permute(0, 2, 1) # Softmax on the permuted tensor
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation to the softmax output.
        return v2
# Inputs to the model
x1 = torch.randn(1, 3, 4)
