
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*32, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model and generating an input tensor to the model:
m = Model()
x1 = torch.randn(3072, 1)
__output__  = m(x1)

