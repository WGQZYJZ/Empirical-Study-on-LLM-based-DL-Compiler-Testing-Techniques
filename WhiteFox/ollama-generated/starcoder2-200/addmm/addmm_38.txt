
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
 
    def forward(self, inp):
        v0 = torch.mm(inp, inp) # Matrix multiplication of two tensors
        v1 = v0 + inp 
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(128, 3, 64, 64)
x2 = torch.randn(128, 3, 64, 64)
__output__  = m(x1, inp= x2)

