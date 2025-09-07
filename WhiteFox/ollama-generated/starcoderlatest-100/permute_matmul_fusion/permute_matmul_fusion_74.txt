
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 8)

    def forward(self, x1):
        v1 = torch.permute(x1, (0, 2, 1)) # Permute the input tensor A
        v2 = torch.bmm(v1, v1)               # Compute batched matrix multiplication
        v3 = torch.matmul(v1, v1)           # Compute dense matrix multiplication
        w1 = torch.nn.functional.linear(v2, self.linear1.weight) # apply linear transformation to the permuted tensor A.
        w2 = torch.nn.functional.linear(v3, self.linear2.weight) # apply linear transformation to the permuted tensor B.
        return torch.cat([w1, w2], dim=1)

# Initializing the model
m = Model()


x1 = torch.randn(1, 2, 2)
