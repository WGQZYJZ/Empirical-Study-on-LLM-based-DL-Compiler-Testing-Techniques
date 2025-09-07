
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x1, y1):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A
        v2 = y1.permute(0, 2, 1) # Permute the input tensor B

        # torch.bmm(v1, v2).shape: [N, 3]

        v4 = self.linear(torch.matmul(v1[:, :, None], v2))
        return v4

m = Model()

x1 = torch.randn(5, 6)
y1 = torch.randn(7, 8)
__output__  = m(x1, y1).shape

