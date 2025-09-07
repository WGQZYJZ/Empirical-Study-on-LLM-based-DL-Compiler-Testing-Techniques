
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, None)  # Apply matrix multiplication between two tensors to an input tensor and add it to the input
        v2 = torch.cat([v1], dim=-1)  # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 1, 1)
