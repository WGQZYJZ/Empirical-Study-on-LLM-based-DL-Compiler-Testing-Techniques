
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.mm(x1[0], x1[2]) # This will fail in CIFAR10
        t2  = torch.cat([t1 for _ in range(9)], 1) 
        return t2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = [torch.randn(8, 5)] * 3 + (np.zeros((40,)),) # This will fail in CIFAR10
__output__   = m(x1)

