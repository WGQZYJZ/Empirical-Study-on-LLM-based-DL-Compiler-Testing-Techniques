
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=0.5): # Keyword argument
        v1 = self.linear(x1) 
        v2 = v1 + other
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3)
other = torch.randn(4) # random input tensor of size (4), which should be the same size as that in "x1"
__output__  = m(x1, other=other)

