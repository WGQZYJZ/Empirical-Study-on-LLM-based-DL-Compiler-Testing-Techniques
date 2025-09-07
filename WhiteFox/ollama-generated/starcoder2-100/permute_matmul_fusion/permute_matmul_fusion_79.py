
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1  = x1.permute(0, 2, 1)
        t3 = torch.bmm(t1, x1)  # or torch.matmul(t1, x1)
        return t3

# Initializing the model
m = Model()
x1 = torch.randn(50, 48*96+24-47, 4)

