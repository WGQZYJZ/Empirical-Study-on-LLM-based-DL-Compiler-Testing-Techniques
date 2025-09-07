
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4, 8)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) # A matrix multiplication between two tensors
        v2 = torch.cat([v1], dim=dim) # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(64, 4)
 