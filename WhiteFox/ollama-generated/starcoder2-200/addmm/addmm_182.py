class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, inp)  # Matrix multiplication on two input tensors with the 'inp' tensor passed as a keyword argument.
        return v1


m = Model()
