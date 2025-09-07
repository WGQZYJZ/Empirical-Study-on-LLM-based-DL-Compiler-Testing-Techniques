
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A and B simultaneously
        v3 = x2.permute(0, 2, 1)

        return torch.bmm(v1, v3)


m = Model()
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 4, 2)
__output__  = m(x1, x2)


