
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.matmul(x1, x3) # Compute the dot product of two input tensors
        return v2

x1  = torch.randn(8, 512)

