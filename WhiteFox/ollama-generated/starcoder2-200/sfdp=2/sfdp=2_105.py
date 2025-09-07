
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and the key 
        return v


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(64, 30)
x2 = torch.randn(30, 78)
__output__  = m(x1, x2)