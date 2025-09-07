
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        v1 = torch.nn.functional.linear(t1, self.linear_A.weight, self.linear_A.bias)

        # The function calls torch.bmm (or torch.matmul) on the permuted tensors to compute the output tensor.
        return torch.bmm(v1, x2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 4, 2)
