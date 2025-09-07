
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(30, 1)

    def forward(self, x):
        v1 = self.linear(x) # Applying linear transformation to the input tensor
        v2 = torch.tanh(v1)# Applying tanh to the output of the linear transformation
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(4,30)
__output__  = m(x)



