
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1) # Permuted tensor A
        v2  = torch.bmm(v1, x2)   # Matrix multiplication on permuted tensors

        v3  = x2.permute(0, 2, 1) # Permuted tensor B
        v4  = torch.bmm(x1, v3)   # Matrix multiplication on permuted tensors (this time, the permute method is invoked only once.)
        v5  = torch.bmm(v4, x2)

        v6  = x2.permute(0, 2, 1) # Permuted tensor B again 
        v7  = torch.bmm(x1, v6)   # Matrix multiplication on permuted tensors (this time, the permute method is invoked twice.)
        return v5 + v4


# Initializing and running the model
m = Model()
x1 = torch.randn(30, 2, 8)
x2 = torch.randn(30, 64, 8) # Input tensor B has more dimensions than input tensors A & B
