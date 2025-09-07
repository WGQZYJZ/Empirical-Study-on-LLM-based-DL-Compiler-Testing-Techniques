
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.addmm(input1, mat1, mat2) # Matrix multiplication with matrix 1 and matrix 2, then adding to the inputs
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()
__input_tensor1__ = torch.randn(3, 64) # Input tensor 1 for the first forward call of the model
__input_tensor2__ = torch.randn(784, 500) # Input tensor 2 for the first forward call of the model
 
# Inputs to the model