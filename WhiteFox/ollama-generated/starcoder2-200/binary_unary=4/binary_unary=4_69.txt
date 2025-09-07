
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(12, 64)
 
    def forward(self, x1, x2=None):
        v1  = self.linear(x1)
        v2  = (v1 + x2) if isinstance(x2, torch.Tensor) else v1
        v3  = F.relu(v2) 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(50, 12)
x2_tensor  = torch.rand((50,), dtype=torch.float32)
x2_int   = int(-1)
__output__  = m(x1, x2_tensor)