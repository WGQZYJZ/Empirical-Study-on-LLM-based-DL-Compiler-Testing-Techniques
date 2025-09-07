
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3072, 4096)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        t1  = torch.addmm(x1, mat1, mat2)
        t2  = torch.cat([t1], dim=1) # Concatenate the result along a specified dimension
        return self.relu(t2)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(3, 4096)
mat1 = torch.randn(385, 3072) # Size is (385, 3072) because 3*385 = 3072, the input size of the model is 3 * 4096.
mat2 = torch.randn(3072, 1)
 
