
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1):
        t2 = torch.full([t1.shape[0], 3], 1, dtype=t1.dtype)  # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(5, 3) # random normal tensors with shape (5, 3)
