
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 512)
 
    def forward(self, x):
        t1 = torch.addmm(x, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim=1) # Concatenate the result along a specified dimension
        v3 = self.linear(t2)
        return v3


# Inputs to the model
x1 = torch.randn(4, 64, 64, requires_grad=True)
