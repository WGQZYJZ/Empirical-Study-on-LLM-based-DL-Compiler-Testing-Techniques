
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 14 * 14, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
v3   = torch.randn(64 * 5).reshape(-1, 32 * 14 * 14)

 # Add other tensor
other_tensor = torch.randn((64*5, ))
 
__output__  = m(x1, other=other_tensor)