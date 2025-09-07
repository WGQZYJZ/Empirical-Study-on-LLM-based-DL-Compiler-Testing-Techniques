
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1) # Permuting input tensor A (2, 2, 4)
        t2 = x1.permute(0, 2, 1) # Permuting input tensor B (2, 2, 4)
        v1 = torch.nn.functional.linear(t1, self.linear1.weight, self.linear1.bias)  # Apply linear transformation to the permuted tensor A (2, 2, 4). 
        v2 = torch.nn.functional.linear(t2, self.linear2.weight, self.linear2.bias)  # Apply linear transformation to the permuted tensor B (2, 2, 4).
        return torch.matmul(v1, v2)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 8)
