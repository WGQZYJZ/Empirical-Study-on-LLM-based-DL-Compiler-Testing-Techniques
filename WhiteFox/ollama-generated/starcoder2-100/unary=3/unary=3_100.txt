
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.relu6(x1)
        v2  = torch.tanh(v1)
        v3  = v1 - v2 + 1 # This line is new!
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)

