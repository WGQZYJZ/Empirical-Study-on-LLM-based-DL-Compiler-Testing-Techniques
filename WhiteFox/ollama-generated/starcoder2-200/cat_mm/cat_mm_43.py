
class Model(torch.nn.Module):
    def __init__(self, n1=3200):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1] * n1, dim=2) # Concatenate the matrix multiplication result along dimension 2
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
n1  = [300 for _ in range(8)] # Generate a list with 8 elements of length 300. The total length is 24,000. 
x1  = torch.randn([1] + n1)
__output__  = m(x1, x1.T)
 
# Expected output: [1, 96000]
 
