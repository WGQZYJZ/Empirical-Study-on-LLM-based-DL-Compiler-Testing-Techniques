
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 1)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = self.sigmoid(v1)
        v3  = v1 * v2 # <-- new_pattern <- new_pattern
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(8, 1024)

# Outputs from the model
__output__  = m(x1)

