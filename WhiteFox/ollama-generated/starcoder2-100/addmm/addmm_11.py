class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2, inp): 
        t1 = torch.mm(input1, input2) # Matrix multiplication on two inputs
        t2 = t1 + inp  # Add the result of matrix multiplication to another tensor 'inp'
        return t2
