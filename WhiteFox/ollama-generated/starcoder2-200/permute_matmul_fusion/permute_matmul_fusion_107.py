
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
       # permute(x) is a method to permutate a tensor. This function takes 2 input arguments: an input tensor (x) and a tuple containing the permutation information which can be used to permute any shape tensor.
        v3 = torch.permute((0, 1), (2, 0)).matmul(y2).bmm(v4).div(self.linear.weight.add(self.linear.bias))
        return v2


# Initializing the model