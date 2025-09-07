
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([2048], 3072) # Create a tensor filled with the scalar value 3072, with 2048 elements
        v2  = convert_element_type(v1, float) # Convert the elements of the tensor to the specified dtype
        v3  = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
__input_x1__ = torch.randn([4], dtype=torch.float64, device='cpu') # A random 2-dimensional array with float values of shape [4] and device 'cpu'
__output__   = m(__input_x1__)
