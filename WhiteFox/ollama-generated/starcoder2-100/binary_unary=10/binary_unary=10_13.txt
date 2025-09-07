
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*32*3, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1.flatten())
        return (v1 + torch.zeros_like(v1)).clamp(-2., .5)


# Initializing the model and generating inputs to it:
m = Model()
x1 = torch.rand(1, 3*32*32)
__output__  = m(x1)