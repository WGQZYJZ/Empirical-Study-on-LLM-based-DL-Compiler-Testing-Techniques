
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.mm(x1, inp) # perform matrix multiplication with the passed input and another input tensor 'inp'
        return v0


# Initializing the model
m  = Model()

# Inputs to the model
input1 = torch.randn(32, 48)
input2 = torch.randn(48, 64)
inp = torch.randn(54, 72).requires_grad_(True)# inp is a matrix with 54 rows and 72 columns

__output__  = m({'x1': input1})

