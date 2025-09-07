
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 3)
        self.linear_B = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = torch.nn.functional.linear(v1, self.linear_A.weight, self.linear_A.bias)
        # v3 is a batch matrix multiplication with dim=1 (or dim=2),
        # which means v3 has shape [n, m] instead of [n, 1].
        v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2).
        v4 = x2.permute(0, 2, 1) # Permute the input tensor B
        v5 = torch.nn.functional.linear(v4, self.linear_B.weight, self.linear_B.bias)
        v6 = torch.bmm(v4, v5) # or torch.matmul(v4, v5).
        return v3 + v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
