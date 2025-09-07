
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(3, 8)
 
    def forward(self, input1):
        v1  = self.attn(input1) + 0.5
        v2  = v1  * v1 * 0.7071067811865476 * torch.erf(v3) 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(1, 3)
__output__  = m(input1)