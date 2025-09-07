
class Model(torch.nn.Module):
    def __init__(self, dim1=320):
        super().__init__()

        self.layer1 = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        return x1.clone()


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(256, 3*32*32).reshape(256, 3, 32, 32)
__output__  = m(x1)
