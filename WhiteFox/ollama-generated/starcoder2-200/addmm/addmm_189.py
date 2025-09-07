
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp): 
        v1 = torch.mm(x1, inp) # Performs matrix multiplication on the input tensors
        v2 = v1 + inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing model 
m = Model()

# Inputs to the model
inp  = torch.randn(5, 3) # The shape of this argument is (5, 3), which is used for performing matrix multiplication on two input tensors in forward function
x1 = torch.randn(3, 4) # Input tensor with size (3, 4). It will be multiplied by the input to the matrix multiplication operator in the forward function


