
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1) # matrix multiplication on two input tensors
        if not inp is None:
            v2 = v1 + self.inp  # Add the result of the matrix multiplication to another tensor 'inp'
        else:
            v2 = v1

        return v2


# Initializing the model with 'inp' as an input argument for its forward() method
m  = Model()
x1, inp  = torch.randn(3, 5), torch.randn(3, 5)
 
# Generating a tensor to pass into the model's 'inp' argument using a torch.nn.Parameter
model_inp = torch.nn.Parameter(torch.rand(3, 4))
m.__setitem__('inp', model_inp)
 
 
# Model with 'inp' argument in its forward() method - outputs tensor of shape [3,5] after applying the matrix multiplication and addition to two input tensors as well as adding the 'inp' parameter
__output___ = m(x1, inp=model_inp)
