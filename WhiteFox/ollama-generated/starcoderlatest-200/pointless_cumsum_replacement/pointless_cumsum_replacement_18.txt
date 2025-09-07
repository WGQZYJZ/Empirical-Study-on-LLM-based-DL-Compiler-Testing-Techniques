
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.size()[0], 1], 1) # Create a tensor filled with the scalar value 1, with the specified dtype and layout
        t2 = convert_element_type(t1, x2.dtype) # Convert the elements of the tensor to the specified dtype
        t3 = torch.cumsum(t2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3
 
