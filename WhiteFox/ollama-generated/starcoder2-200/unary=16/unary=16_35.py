
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128, 64)
 
    def forward(self, x1):
        v0 = torch.relu(self.linear(x1)) # Apply ReLU activation to the output of a linear transformation on x1
        return v0


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(2, 128)
__output__  = m(x1)

