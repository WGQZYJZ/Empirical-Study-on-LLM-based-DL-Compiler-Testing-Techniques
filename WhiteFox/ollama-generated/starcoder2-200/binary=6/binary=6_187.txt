
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other 
        return v2


# Initializing the model
m = Model()
other  = (torch.ones([3]) * 4)[None].reshape((1, 3))
print('other.shape', other.shape)
 
# Inputs to the model
x1 = torch.randn(1024, 256)
__output__  = m(x1).argmax(-1)

