
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(10,8)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5
        return v6

 # Initializing the model
 m = Model()
 
 # Inputs to the model
  x1  = torch.randn(1,10)
 __output__  = m(x1)

# Input tensor
# [[-0.37459484 -0.3563981  -0.0563205   0.1348083   0.32928527
#   -0.33542847 -0.12637881 -0.0356604  -0.3540206  -0.17684439]]

