
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        t1 = torch.mm(input1, input2)
        t2  = t1 + inp
        return t2


# Initializing the model with an initial tensor 'inp' as a keyword argument.
m = Model()
inp  = torch.randn(4096, 5783) # 'inp' is the initial tensor that will be used as a keyword argument for the forward method of the model
__output__  = m(x1=inp, x2=inp)

