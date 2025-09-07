
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.empty([256], requires_grad=True)
        v1 = 3 * (v0.pow(2))
        v2 = 3 * ((-3)*x1) + v1
        v4 = v2.sum()
        v3 = torch.addmm(v1, mat1, x1)
        v5 = torch.cat([v3], -1).to(torch.float64)
        return v0


# Initializing the model
m  = Model()

# Inputs to the model
mat1 = torch.randn(256, 789, dtype=torch.float64)
x1 = torch.randn(3, 4).to(torch.float64)
 
# Compute output for this input
__output__  = m(x1)

