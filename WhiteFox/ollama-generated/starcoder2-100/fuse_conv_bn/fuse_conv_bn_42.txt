
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        return self.conv3d_1(x1)

m = Model()
x1  = torch.randn(2, 100, 564876999999) # A non-valid input tensor that causes the issue.
__output__  = m(x1)


