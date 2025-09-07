
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1=5000):
        v1 = torch.full([arg1, 2], 1) # Create a tensor filled with the scalar value 1
        v2 = convert_element_type(v1, torch.int64) # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, 0) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v3

# Initializing the model
m = Model()

