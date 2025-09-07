
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None):
        return torch.mm(x1, x2) + inp  # Add the result of the matrix multiplication to another tensor 'inp'

# Initializing model
model = Model()

# Input tensors to the model
input_tensor1 = torch.randn((30,5))
input_tensor2 = torch.randn(5,4)

