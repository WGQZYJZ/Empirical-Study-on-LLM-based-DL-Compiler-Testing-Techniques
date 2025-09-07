
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 32, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 64*32))
        v2  = (v1 > 0).to(torch.bool) 
        v3  = v1 * -0.1 
        v4  = torch.where(v2, v1, v3) 
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model 
x1 = torch.randn(8, 5*64*32).requires_grad_(True) 

# Creating a gradient graph for the inputs and running the forward pass
with torch.enable_grad():
    __output__  = m(x1)

