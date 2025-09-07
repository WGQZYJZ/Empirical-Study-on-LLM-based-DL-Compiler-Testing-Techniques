
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        v1  = torch.full([3, 5], 1, dtype=torch.float64) # Create a tensor filled with the scalar value 1, with the specified dtype
        v2  = v1 * v1  # Multiply two tensors elementwise
        v3  = convert_element_type(v1, torch.int8)  # Convert the elements of the first tensor to int8
        return v2, v3


# Initializing the model
m  = Model()


# Inputs to the model: 
__input_1__  = torch.randn([50]) # A random 1D tensor with 50 elements
__input_2__  = torch.randn([3, 64, 64], dtype=torch.float32) # A random 3-dimensional tensor of shape [3, 64, 64] and dtype float32
__input_3__  = torch.randint(50, (1,), device="cuda") # An integer 1D tensor with one element
__output__  = m(__input_1__, __input_2__, __input_3__)

