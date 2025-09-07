
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.func([x1])
        v3 = torch.cat(v2) # Concatenate the output of func() along dimension 0 
        return v3
 
    @staticmethod
    def func(args):
        return [torch.randn(*args)]


# Initializing the model
m = Model()

# Inputs to the model, shape as (3,)
x1  = torch.randn(3)
 
__output__  = m(x1)
