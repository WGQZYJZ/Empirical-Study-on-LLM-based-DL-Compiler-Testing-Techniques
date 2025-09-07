
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*64*64, 1)
 
    def forward(self, x1):
        v0  = x1.reshape(-1, 3 * 64 * 64)
        v1  = self.linear(v0)
        v2  = v1 + other_tensor
        return v2


# Initializing the model
m = Model()
other_tensor  = torch.randn(1, 8*8*3).cuda()


# Inputs to the model
x1  = torch.randn(1024, 64) + other_tensor
__output__  = m(x1)

