
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 4096)
 
    def forward(self, x1):
        l1 = self.linear(x1) 
        l2 = l1 * clamp(min=0, max=6, l1 + 3) # multiply the output of the linear transformation by the clamped output of the linear transformation added with 3
        l3 = l2 / 6  
        return l3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1,512)
__output__  = m(x1)

