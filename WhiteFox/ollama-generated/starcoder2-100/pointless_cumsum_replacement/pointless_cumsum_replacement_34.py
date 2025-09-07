
class Model(torch.nn.Module):
    def __init__(self, arg1: int, arg2: str):
        super().__init__()
 
    def forward(self, x1: torch.Tensor):
        t1 = torch.full([arg1, arg2], 1) # Create a tensor filled with the scalar value 1 (here: argument `arg2`)
        t2 = t1.float() # Convert the elements of the tensor to float type
        t3 = t2.cumsum(dim=0).float() # Compute the cumulative sum of the elements of the tensor along dimension 0, and convert them to a new tensor with float type
 
        return t3

# Initializing the model
m = Model(10, 'float')


# Inputs to the model
x1 = torch.randn(20)
__output__  = m(x1)