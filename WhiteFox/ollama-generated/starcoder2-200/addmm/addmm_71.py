
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor, x2: torch.Tensor):  # x1 and x2 are tensors in PyTorch
        out = torch.mm(x1, x2) + inp   # Add result of matrix multiplication to another tensor 'inp'
        return out


# Initializing the model
m = Model()
 
# Inputs to the model
__input_tensor__  = torch.randn(3, 4)  # A dummy tensor
inp = torch.randn(50,)    # A tensor passed as a keyword argument 

