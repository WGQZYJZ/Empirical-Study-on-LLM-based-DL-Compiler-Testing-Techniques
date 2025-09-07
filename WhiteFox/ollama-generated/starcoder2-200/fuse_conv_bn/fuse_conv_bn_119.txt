
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.conv2d(x1, self.linear.weight)
        v  = torch.nn.functional.batch_norm(v)

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 28, 28) # A dummy input for the model initialization 

__output__  = m(x1)
