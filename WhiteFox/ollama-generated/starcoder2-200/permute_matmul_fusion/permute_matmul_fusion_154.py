
class Model(torch.nn.Module):
    def __init__(self, inshape1, inshape2):
        super().__init__()

    def forward(self, x1, x2):
        v3 = torch.bmm(x1, self.__your_permuted__tensor_from_x2_here) # or torch.matmul(x1, self.__your_permuted__tensor_from_x2_here)
        return v3


# Initializing the model with proper input shape
m  = Model(inshape1=2, inshape2=4)

# Inputs to the model: 
x1 = torch.randn(*inshape1)
x2 = torch.randn(*inshape2)
