
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = self.linear(x1) # Linear transformation is applied to an input tensor
        v2 = 3 + v1 - 7   # A tensor or scalar is subtracted from the output of the linear transformation
        return v2, v1 # The outputs are both returned

m = Model()
__output__, v1  = m(x1)

