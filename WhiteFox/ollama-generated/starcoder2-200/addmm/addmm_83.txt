
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None): 
        v1 = torch.mm(x1, inp)
        v2  =v1 +inp
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5, 7)# Tensor that represents the first matrix in the input of the model. It is randomly generated from a normal distribution with mean 0 and variance 1
inp=torch.ones(6, 9) # Tensor that represents the second matrx in the input of the model. It is randomly generated from a normal distribution with mean 0 and variance 1
