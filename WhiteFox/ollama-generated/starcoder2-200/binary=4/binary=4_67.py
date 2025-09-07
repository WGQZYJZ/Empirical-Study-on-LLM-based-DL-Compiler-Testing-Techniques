class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2
m  = Model()
x1  = torch.randn(568937, 10) # An input tensor with 568937 rows and 10 columns
__output__  = m(x1)

