
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2a = (v1 > 0).to(dtype=torch.float32) # where v1 is the output of linear transformation
        v3  = torch.where((v2a == True), v1, -0.5 * v1 + 0.7071067811865476) 
        return v3
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(128, 3)
 
 __output__  = m(x1)

