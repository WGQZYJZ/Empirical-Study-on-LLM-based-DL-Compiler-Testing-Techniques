
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication between the first input and the second input
        v2 = torch.mm(v1 + 0, v2 + 3) # Addition of zeros to the output of the matrix multiplication resulting from the first two inputs and addings 3s to the output of the matrix multiplication resulting from the third fourth inputs
        return v1


# Initializing the model
m = Model()

# Inputs to the model
__inputs__  = [torch.randn(4,5), torch.randn(20,8)]
__output__  = m(*__inputs__)

