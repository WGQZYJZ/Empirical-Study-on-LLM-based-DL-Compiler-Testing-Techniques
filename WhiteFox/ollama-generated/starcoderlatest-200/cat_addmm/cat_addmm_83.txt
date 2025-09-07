
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2) # Perform matrix multiplication of two tensors and add it to the first tensor
        v2 = torch.cat([v1], dim=0) # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(5, 3, 64, 64)
