
class Model(torch.nn.Module):
    def __init__(self, splitDim = 1):
        super().__init__()
        
    def forward(self, x1):
        s0, s1, s2  = torch.split(x1, 32, dim= self.__split_dim__ )
        c = torch.cat([s0 , s2], dim = splitDim)
        return c
# Initializing the model and setting the dimension along which to perform the split/concat operations.

m  = Model(splitDim = 1)


x1 = torch.randn(48,3,64,64)
__output__  = m(x1)

