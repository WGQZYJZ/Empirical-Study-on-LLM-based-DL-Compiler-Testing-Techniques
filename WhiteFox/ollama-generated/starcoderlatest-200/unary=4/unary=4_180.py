
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # view() is a method of Tensor to convert the data in an n-dimensional matrix (the default) into an (n-1)-dimensional tensor. For example, given a tensor with 3 dimensions [a, b, c], we can view it as a two dimensional matrix through: v2 = x.view(1, -1), where the -1 indicates to view the last dimension to be all the remaining dimensions into one single dimension.
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
