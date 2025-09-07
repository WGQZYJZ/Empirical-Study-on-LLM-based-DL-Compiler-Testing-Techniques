
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v0 = torch.mm(x1, self.weights) # Matrix multiplication on 2 input tensors 
        return v0 + inp
 
# Initializing the model with randomly generated weights
m = Model()
m.weights = torch.randn((8465376,), requires_grad=True).view(9184, 907)

# Inputs to the model - two tensors as input and a 'inp' tensor as keyword argument
x1  = torch.randn(128, 9184) # The first tensor is randomly generated with shape [batch_size x input size]
inp = torch.randn(907,)      # The 'inp' is randomly generated with shape [output size]
__output__  = m(x1, inp=inp)

