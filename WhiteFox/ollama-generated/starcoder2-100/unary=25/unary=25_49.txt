
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = (v1 > 0).to(torch.float32)
        v3  = v1 * negative_slope 
        v4  = torch.where(v2, v1, v3)
        return v4
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1024, 32)

 # Outputs from the model 
 __output__  = m(x1)
