
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 5)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3

# Initializing the model
m  = Model()
other = torch.tensor([[-0.5, -1.,  2.,   4.,    6.]]) # The `other` tensor


# Inputs to the model
x1  = torch.randn(8, 3)
__output__  = m(x1, other=other)