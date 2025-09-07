
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v3 = torch.bmm(x1, y2)  # or torch.matmul(x1, y2)
        return v3


m  = Model()
x1 = torch.randn(1, 4, 8, 5, 6)
y2 = torch.randn(1, 7, 9)

__output__  = m(x1, y2)

# Initializing the model
