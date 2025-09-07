
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2) 
        v2 = v1 + inp  # Add the result of the matrix multiplication to another tensor 'inp'

        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(300, 589)
x2 = torch.randn(300, 589) # x2 is not used in this model
inp = torch.randn(4, 576)
__output__  = m(x1, inp)

