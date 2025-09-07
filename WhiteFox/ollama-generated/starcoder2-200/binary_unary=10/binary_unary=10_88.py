
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 144, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other # Replace with another tensor that exists in the environment.
        v3  = torch.relu(v2)
        return v3

# Initializing model
m = Model()

# Inputs to the model
x1  = torch.randn(64, 32 * 144)
__output__  = m(x1)

