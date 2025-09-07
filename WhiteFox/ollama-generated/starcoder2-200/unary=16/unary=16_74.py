
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*16, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = nn.functional.relu(v1)
        return v2

# Initializing the model
m  = Model()
 
# Input to the model
__input__ = torch.randn(8,32*16) 
 
__output__= m(__input__)

