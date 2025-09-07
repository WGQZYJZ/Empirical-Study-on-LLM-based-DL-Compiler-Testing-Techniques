
class Model(torch.nn.Module):
    def __init__(self, arg1=None, arg2=None):
        super().__init__()
 
    def forward(self, x0):
        t1 = torch.full([arg1, arg2], 1, dtype=torch.float32)
        t2 = t1.to('cuda')
        __output__  = self.__call__(t2)


# Initializing the model with custom arguments `arg1` and `arg2`. 
m = Model(arg1=8, arg2=4)

x0 = torch.randn(563, 791, dtype=torch.float32).to('cuda')

 # Inputs to the model. The tensors should be different from the previous ones or there will be an error `AssertionError`.

# +
x1 = x0

__output__  = m(x1)
# -




