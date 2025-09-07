
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2=None):
        v1 = None # input tensor A
        if x2 is not None:
            v1 = x1.permute(0, 2, 1)  # permute tensor A
        else:
            v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)  # linear transformation on tensor A

        v2 = None # input tensor B
        if x2 is not None:
            v2 = x2.permute(0, 2, 1)  # permute tensor B
        else:
            v2 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)  # linear transformation on tensor B

        v3 = None  # output from torch.bmm or torch.matmul
        if x2 is not None and x1 is not None:
            v3 = torch.bmm(v1, v2) # compute result of matrix multiplication
        elif x1 is not None and x2 is not None:
            v3 = torch.bmm(v2, v1)  # compute result of matrix multiplication
        else:
            assert False

        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = None if __input_tensor__[0] == x1 else torch.randn(1, 2, 2)
