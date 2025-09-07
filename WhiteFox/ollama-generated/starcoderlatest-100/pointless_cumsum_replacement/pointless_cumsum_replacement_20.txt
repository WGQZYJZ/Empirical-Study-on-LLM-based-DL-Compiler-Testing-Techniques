
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.full([4, 6], 0.0, dtype=x.dtype, layout=x.layout, device=x.device) # Create a tensor filled with the scalar value 0.0, with the specified dtype, layout, and device
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # input tensor for model
