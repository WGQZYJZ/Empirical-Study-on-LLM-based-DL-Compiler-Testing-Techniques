
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], 1], 1)  # Create a tensor filled with the scalar value 1 for each element in each row of the specified shape, and the dtype as input
        v2 = convert_element_type(v1, x2.dtype) # Convert the elements of the tensor to the dtype specified by `x2`
        v3 = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
input_tensor = torch.randn([1, 3, 64, 64])
input_dtype  = input_tensor.dtype
