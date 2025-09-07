
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 1024)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.addmm(v1, mat1, mat2) # Concatenate the result along a specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64)
mat1 = torch.randn(32, 512)
mat2 = torch.randn(512, 64)
