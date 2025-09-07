
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.dim  = dim
        self.fc1  = torch.nn.Linear(8*8*3, 4)
 
    def forward(self, x):
        v0  = x
        v1  = torch.addmm(v0, mat1, mat2)
        v2  = torch.cat([v1], self.dim) # Concatenate the result along dimension dim
        return v2


# Initializing the model
m  = Model()
