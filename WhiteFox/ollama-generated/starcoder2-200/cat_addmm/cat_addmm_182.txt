
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1)  # A matrix multiplication of input and matrices
        v2 = torch.cat([v1], dim) 
        return v2

# Initializing the model
m = Model()

