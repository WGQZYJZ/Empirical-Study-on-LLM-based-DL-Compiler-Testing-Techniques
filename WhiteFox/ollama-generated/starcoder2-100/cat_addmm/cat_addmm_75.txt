
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.cat  = nn.ConcatDim(dim=dim)

    def forward(self, x1, y1):
        v1  = self.conv(x1)
        v2  = torch.addmm(v1, y1) # This is where the matrix multiplication takes place
        v3  = self.cat([v2]) # This is where the concatenation takes place
        return v3

# Initializing and running model
m  = Model()
x1  = torch.randn(10, 3, 64, 64)
y1  = torch.randn(10, 8, 64, 64)
__output__  = m(x1, y1)
