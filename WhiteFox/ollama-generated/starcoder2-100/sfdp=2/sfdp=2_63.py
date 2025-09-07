__input__   = torch.randn(1, 50, 10)       # Input tensor of size (1, batchsize x sequence_length x embedding dimensions) 
__output__  = model(__input__)               # Model output (softmaxed dot product of query/key, and value) with a shape of (batchsize x sequence length x output dimensionality). 
                                             # The batchsize is 1 here. Therefore it is necessary to take the last dimension as an argument for softmax.
v1 = torch.matmul(x, key.transpose(-2, -1)) # Compute the dot product of a query and a key 
v2 = v1 * scale_factor                      # Multiply the dot product by another constant 

## Description of requirements
The model should contain the following pattern:

 This pattern characterizes scenarios where a pointwise activation is applied on an input. For example, we could apply the LeakyRelu function to add three to an input and then divide it by that same input in the resulting operation.

 # Model:
class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
       return torch.nn.LeakyReLU()(t1 + 3.) / t1
