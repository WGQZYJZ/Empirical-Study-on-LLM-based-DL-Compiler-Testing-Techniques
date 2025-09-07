
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(1024, 1)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2  * v5
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(10, 8*8*3)

 # Initializing a list of output values before calling the model:
__outputs__  = [0] * m.__call__(torch.ones(4)).shape[-1] 
