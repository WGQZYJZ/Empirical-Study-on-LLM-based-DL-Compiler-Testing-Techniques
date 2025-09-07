
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 256)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(10, 10)
__output__   = m(x1)

# The other tensor that is passed as a keyword argument (i.e., the "other" in the forward method)
other_tensor  = torch.randn(256,)

