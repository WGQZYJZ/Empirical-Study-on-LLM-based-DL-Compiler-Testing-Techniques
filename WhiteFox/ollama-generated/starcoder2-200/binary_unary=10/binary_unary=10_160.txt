
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3 * 64 **2, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = other + v1 
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
__input__   = torch.randn(4, 3 * 64 **2 )
 
