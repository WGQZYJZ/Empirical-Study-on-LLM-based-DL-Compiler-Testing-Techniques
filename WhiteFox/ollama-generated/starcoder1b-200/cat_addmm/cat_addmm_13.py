
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear1 = torch.nn.Linear(3072, 5)
        self.linear2 = torch.nn.Linear(5, 64)
 
    def forward(self, x1, mat1, mat2):
        t1 = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim=dim) # Concatenate the result along a specified dimension
        return self.linear2(self.linear1(t2))
# Initializing the model
m = Model(1)


