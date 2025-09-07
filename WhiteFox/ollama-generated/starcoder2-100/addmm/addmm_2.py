
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp): 
        v1 = torch.mm(*inp) + inp[2]  # Perform matrix multiplication on two input tensors and add the result of this operation to another tensor 'inp'
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
inp = (torch.randn(3, 4), torch.randn(2, 8), torch.rand(3, 4))
__output__  = m(*inp)
