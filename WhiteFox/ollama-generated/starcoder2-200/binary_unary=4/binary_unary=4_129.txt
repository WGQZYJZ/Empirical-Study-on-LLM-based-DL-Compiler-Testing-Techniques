
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other):
        v1  = torch.nn.Linear(x1).weight + other
        v2  = F.relu(v1)

        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(5, 4096)
 other = torch.randn(3784, 4096)
 
 __output__  = m(x1, other)
