
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1], 1) # Create a tensor filled with the scalar value 1
        v2 = convert_element_type(v1, dtype=torch.float32) # Convert the elements of the tensor to float32
        v3 = torch.cumsum(v2, dim=-1) # Compute the cumulative sum of the elements of the tensor along dimension -1
        return v3


# Initializing the model
m = Model()

