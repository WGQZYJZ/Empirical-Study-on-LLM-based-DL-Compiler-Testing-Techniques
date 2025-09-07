
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Parameter(torch.randn(3, 64 * 64))
        self.matmul2 = torch.nn.Parameter(torch.randn(64, 8))
 
    def forward(self, x1):
        v1 = self.matmul1.t().mm(x1) # Apply a matrix multiplication of matmul1 and x1
        v2 = torch.cat([v1], dim=0)
        return self.matmul2.t().mm(v2)
 
# Initializing the model
m = Model()
 
 # Inputs to the model
 x1 = torch.randn(64, 3, 64, 64)
 