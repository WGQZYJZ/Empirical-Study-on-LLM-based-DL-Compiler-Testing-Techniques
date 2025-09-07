
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8 * 8 * 3, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + other_tensor # Adding another tensor to the result of a linear transformation
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
other_tensor  = torch.rand(8 * 8 * 3, dtype=torch.float64) # A random tensor to be added to the output of a linear transformation
# Inputs to the model
x1  = torch.randn(1024, 8 * 8 * 3)


__output__   = m(x1).sum()


