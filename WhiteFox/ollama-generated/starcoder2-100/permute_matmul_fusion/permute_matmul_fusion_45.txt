
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.randn(4)  # Input tensor A
        t2 = torch.randn(5)  # Input tensor B

        v1 = x1.permute(0, 2, 1).bmm(x2)
        return v1

# Initializing the model