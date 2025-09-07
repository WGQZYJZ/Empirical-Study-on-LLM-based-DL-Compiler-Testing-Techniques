
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.mm(x1)  # Perform matrix multiplication on the input tensor without passing 'input' as a keyword argument 
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 4)
x2  = torch.randn(4, 5)
inp = torch.randn(3, 6) 
 