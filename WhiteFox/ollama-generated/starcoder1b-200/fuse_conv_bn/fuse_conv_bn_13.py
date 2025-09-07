
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.convXd(...)  # X can be 1, 2, or 3 representing the dimension
        bn1 = torch.nn.functional.batch_norm(...)  # X should match with ConvXd
        v2 = torch.nn.functional.linear(v1, bn1.weight, bn1.bias)  # Apply linear transformation to the permuted tensor
        return v2


# Initializing the model
m = Model()

