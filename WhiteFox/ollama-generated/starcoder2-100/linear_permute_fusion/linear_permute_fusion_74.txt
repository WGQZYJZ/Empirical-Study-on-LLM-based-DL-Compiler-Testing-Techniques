

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight)
        v2 = v1.permute(-1, -2, 0, 1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 5, 6) # input tensor should contain 3 dimensions (2d) with more than two axes and more than one element.
weight = torch.randn(3, 8096) # linear layer weights need to be random, since we are going to generate a permuted output from the permute operation on the permuted input tensor.
m.weight = weight


__output__|end_of_text__  = m(x1)
