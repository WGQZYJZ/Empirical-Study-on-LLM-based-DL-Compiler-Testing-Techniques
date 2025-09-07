
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 10)
 
    def forward(self, x):
        v1  = self.linear(x) # Apply a linear transformation to the input tensor
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) 
        v4  = torch.clamp_max(v3, 6)
        v5  = v4 / 6
        return v5

# Initializing the model and setting the weights to some random values.
m1 = Model()
for p in m1.parameters():
    p.data[...] = torch.randn(p.shape)
 
# Inputs to the model
x = torch.rand(3, 4096)


