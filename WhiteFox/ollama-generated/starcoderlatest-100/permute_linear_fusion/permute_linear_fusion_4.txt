
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # permute the input tensor
        v2 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias) # apply linear transformation to the permuted tensor
        return torch.add(v2, self.linear2.weight[0]) # add a constant value to the linear transformation result


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
