
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp):
        t1 = torch.mm(inp[0], inp[1])  # Perform matrix multiplication on two input tensors
        t2 = t1 + inp[2]  # Add the result of the matrix multiplication to another tensor 'inp'
        return t2


# Initializing the model and passing the keyword argument
m = Model()
x = (torch.randn(3, 4), torch.randn(4, 5), torch.randn(5, 6))
