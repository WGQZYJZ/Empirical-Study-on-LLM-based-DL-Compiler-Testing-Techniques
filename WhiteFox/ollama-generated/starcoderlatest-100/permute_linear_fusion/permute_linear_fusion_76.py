
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3) # <== The last dimension is swapped with the second-to-last one in order to apply linear transformation to the permuted tensor. 
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2, 2) # The last dimension in this tensor is swapped with the second-to-last one in order to apply linear transformation on it.
