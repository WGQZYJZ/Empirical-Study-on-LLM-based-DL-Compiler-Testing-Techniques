
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp=None):
       t1 = torch.mm(x1, x2) # Matrix multiplication on two input tensors
       t2  = t1 + inp  # Add the result of the matrix multiplication to another tensor 'inp' 
       return t2
 
m = Model()

