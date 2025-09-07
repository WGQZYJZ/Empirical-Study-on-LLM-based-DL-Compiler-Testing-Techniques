
class Model(torch.nn.Module):
    def __init__(self, n1, n2):
        super().__init__()
        self.weight1  = torch.nn.Parameter(torch.randn((n1, n2)))
 
    def forward(self, x1):
        w1 = self.weight1 # Initialize a new parameter that is the output of this model with the same shape as weight1
        t1  = torch.mm(x1, w1) 
        t2 = torch.mm(w1.t(), t1) 
        t3 = t2 + x1 * 5 # Multiply each entry of x1 by a constant 5 and add it to the matrix multiplication of the transposed weight parameter times the output of this model
        return t3


# Initializing the model with input shape: (64, 8)
n1 = 64
n2 = 8
m = Model(n1, n2)

__input_tensor__ = torch.randn((n1, n2))
__output__  = m(__input_tensor__)
