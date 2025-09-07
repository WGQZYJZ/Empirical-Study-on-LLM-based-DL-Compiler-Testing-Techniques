

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, inp=None):
        v1  = torch.mm(input1, input2) # Matrix multiplication on two input tensors 
        v2  = v1 + inp # Add the result of matrix multiplication to another tensor 'inp'
        return v2
 
m = Model()


__output__  = m(x1, x3)

