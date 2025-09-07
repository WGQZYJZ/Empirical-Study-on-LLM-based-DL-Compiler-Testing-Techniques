
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.linear = torch.nn.Linear(n, 1)
 
    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], dim=0)
        return self.linear(v2)


# Initializing the model with 64 units in the fully connected layer
m  = Model(n=64)


