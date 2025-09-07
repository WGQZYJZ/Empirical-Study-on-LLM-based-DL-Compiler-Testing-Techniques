
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2): # Input shape: (batch_size * 4, 5)
        v3 = torch.mm(x1, y1) 
        v4 = torch.mm(x2, y2) 
        v6 = v3 + v4
        return v6

# Initializing the model
m  = Model()
__input_tensor_shape__  = (5,) # input tensor for model
__input_tensor1_shape__  = __input_tensor_shape__, 20  # input shape of input1 matrix in the model. It should be different from the input shape above.
__input_tensor4_shape__  = __input_tensor_shape__, 5   # input shape of input4 matrix in the model. It should be different from the input shape above.


# Inputs to the model
x1, y1, x2, y2  = torch.randn(batch_size, 5), torch.randn(batch_size, 20), \
                  torch.randn(batch_size, 5), torch.randn(batch_size, 5)
__output__  = m(x1, y1, x2, y2) # The shape of output should be different from the shape above

# Output shape
__output_shape__ = batch_size, 40

