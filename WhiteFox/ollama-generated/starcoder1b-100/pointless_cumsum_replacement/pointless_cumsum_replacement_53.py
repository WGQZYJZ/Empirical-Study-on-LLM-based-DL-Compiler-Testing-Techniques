
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t2 = torch.tensor([[1]], dtype=torch.long)
 
    def forward(self, x1):
        v1  = convert_element_type(x1, dtype=torch.double) # Convert elements of the input tensor to the double type
        v2 = torch.cumsum(v1, 1) # Compute the cumulative sum of the elements along dimension 1
        return v2


# Inputs to the model
__input__  = torch.randn(1, 3, 64, 64)
x1     = __input__.double() # Convert input tensor from the float type to the double type
