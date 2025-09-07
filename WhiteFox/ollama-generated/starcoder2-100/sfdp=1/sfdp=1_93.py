class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.nn.functional.gelu(x1)


m = Model()
__output__  = m(torch.randn(4, 5))

