
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.full([x.shape[0], 8, 26, 5], 1, dtype=dtype) # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(128, 3, 64, 64)
