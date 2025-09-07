
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.bmm
        self.matmul = torch.matmul

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        return self.bmm(v1, x2).permute(0, 2, 1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 4)
x2 = torch.randn(5, 6)
