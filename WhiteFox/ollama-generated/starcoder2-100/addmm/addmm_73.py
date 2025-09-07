
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + 100 # 'inp' is passed as a keyword argument for the matrix multiplication
        return v2

# Initializing the model
m = Model()


# Inputs to the model
inp  = [torch.randn(3, 4), torch.randn(4, 5)]
__output__  = m(*inp)
