
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        if inp == None:
            t1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        else:
            t1 = torch.mm(x1, inp)  # If an 'inp' keyword argument is passed in the forward() function, perform the operation on the second input tensor
        t2 = t1 + 0
        return t2


# Initializing the model and specifying the optional keyword arguments
m = Model()
m(x1, inp=torch.randn(16)) # Pass a constant '0' as value for the optional 'inp' keyword argument


