
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32, 800)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other
        v3  = F.relu(v2) 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 32 * 32) # a 4 × 50,000 tensor representing 32 x 32 images. 
__output__  = m(x1)