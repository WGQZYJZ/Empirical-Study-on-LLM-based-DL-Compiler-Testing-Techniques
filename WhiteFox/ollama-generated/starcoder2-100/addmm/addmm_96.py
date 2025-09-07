
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.linear
 
    def forward(self, x1, x2, **kwargs):
        v1  = self.mm(x1, x2) # Applying a matrix multiplication on two input tensors 'x1' and 'x2'.
        v2  = v1 + kwargs['inp'] 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 4) # Random matrix for  input1 with size [N x M] where N and M are constants.
x2  = torch.randn(4, 5) # Random matrix for  input2 with size [M x P] where P is a constant.
inp  = torch.randn(3, 6) # Constant input tensor 'inp' which is not used in the 'forward' function of our model but is passed as a keyword argument.


__output__  = m(x1, x2, inp=inp)

