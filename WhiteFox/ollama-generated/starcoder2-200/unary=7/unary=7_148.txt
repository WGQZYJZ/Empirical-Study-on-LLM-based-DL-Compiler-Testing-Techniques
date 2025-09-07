
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 3136)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to the input tensor
        v2  = clamp(min=0, max=6, t1 + 3) # Clamped between 0 and 6 output of the linear transformation added with 3 
        v3  = v2 / 6 # Divide by 6 
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2048)
__output__  = m(x1)


