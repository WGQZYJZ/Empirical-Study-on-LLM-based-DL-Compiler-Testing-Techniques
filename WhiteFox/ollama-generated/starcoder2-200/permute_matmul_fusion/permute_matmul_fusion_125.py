
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, y):
        v1 = x1.permute(0, 2, 1)
        v3 = v1 * y # or torch.matmul(v1, y)

        # We want to find the output value of torch.nn.functional.linear function after permuted tensor.
        v4 = torch.nn.functional.linear(
            v3, self.linear.weight, self.linear.bias).squeeze(-1)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(256, 2, 200) # input_tensor A: tensor with shape [B x M x N] where B is batch size; M and N are the number of columns in matrix A or rows in vector A.
y   = torch.rand(1, 1, 384)    # Input tensor B

__output__  = m(x1, y) # output from model: shape [B x M] where B is batch size and M the number of columns in matrix B.