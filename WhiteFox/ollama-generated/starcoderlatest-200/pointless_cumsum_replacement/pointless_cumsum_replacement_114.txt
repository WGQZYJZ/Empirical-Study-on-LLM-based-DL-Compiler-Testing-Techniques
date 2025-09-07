
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=x1.dtype) # Create a tensor filled with the scalar value 1, with the specified dtype
        t2 = convert_element_type(t1, x2.dtype)  # Convert the elements of the tensor to the specified dtype
        t3 = torch.cumsum(t2, 1)  # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randint_like(x1, 50).to(device)
