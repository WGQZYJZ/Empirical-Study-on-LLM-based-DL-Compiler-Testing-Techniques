
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # Swap the last two dimensions of this tensor
        v2 = torch.nn.functional.relu(torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)) # Apply linear transformation to the permuted tensor.
        return torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias)
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
