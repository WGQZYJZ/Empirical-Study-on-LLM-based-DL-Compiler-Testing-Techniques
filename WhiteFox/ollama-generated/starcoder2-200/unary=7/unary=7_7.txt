
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(30, 24)
 
    def forward(self, x):
        v1  = self.linear1(x)
        v2  = F.selu(v1 + 3) / 6
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x_shape = (50, 30) # Shape of input tensor
x = torch.randn(*x_shape)
__output__  = m(x)

