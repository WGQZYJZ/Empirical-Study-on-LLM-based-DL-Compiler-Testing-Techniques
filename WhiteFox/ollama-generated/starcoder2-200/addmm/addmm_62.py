
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, inp):
        v1 = torch.mm(input1, input2) # Matrix multiplication on two tensors
        v2 = v1 + inp  # Matrix multiplication output is added to another tensor 'inp'
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
inp_tensor  = torch.randn(4, 4)
tensorA  = torch.randn(4, 5000)
tensorB  = torch.randn(4, 5001)
 
# Forward pass
__output__  = m(tensorA, tensorB, inp_tensor)

