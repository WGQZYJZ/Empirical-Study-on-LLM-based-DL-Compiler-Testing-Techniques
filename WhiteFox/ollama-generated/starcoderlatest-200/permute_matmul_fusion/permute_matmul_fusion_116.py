
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 2)
        self.linear_2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = x2.permute(0, 2, 1) # Permute the input tensor B
        t3 = torch.bmm(v1, v2)   # Apply batch matrix multiplication on two permuted tensors to get a result of shape [batch_size, C]
        u1 = torch.nn.functional.linear(t3, self.linear_1.weight, self.linear_1.bias)
        u2 = torch.nn.functional.linear(u1, self.linear_2.weight, self.linear_2.bias) # Apply linear transformation to the result of `torch.bmm`
        return u2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
