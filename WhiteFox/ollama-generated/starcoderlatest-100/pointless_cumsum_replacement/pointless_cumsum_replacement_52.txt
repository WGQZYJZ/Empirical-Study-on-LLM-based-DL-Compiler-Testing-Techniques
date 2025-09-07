
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor):
        v1 = torch.full([input_tensor.shape[0], 1], 1, dtype=input_tensor.dtype)
        v2 = convert_element_type(v1, input_tensor.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
