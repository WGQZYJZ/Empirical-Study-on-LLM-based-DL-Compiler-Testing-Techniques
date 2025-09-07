
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        y = torch.mm(x1, inp) + 5 # Multiply the result of matrix multiplication by another tensor 'inp' and add it to the result of multiplying the result of matrix multiplication by itself
        return y


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
inp  = torch.randn(2, 5)
