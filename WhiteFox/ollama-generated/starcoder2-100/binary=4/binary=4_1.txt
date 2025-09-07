
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.rand(v1.size())
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor  = torch.randn(5, 20)
__output__   = m(input_tensor)