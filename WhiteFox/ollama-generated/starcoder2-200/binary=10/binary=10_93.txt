

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other_tensor
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 
__output__  = m(torch.randn(640))
