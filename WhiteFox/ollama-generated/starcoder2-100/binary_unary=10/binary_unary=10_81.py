
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(807234, 51)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2) # Other tensors added to the ReLU
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(807234, 65)

# Output of the model
__output__  = m(x1)
