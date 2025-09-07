
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 8)
 
    def forward(self, x):
        v1  = self.linear(x) 
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(64, 8)

# Other tensor for input/output matching
other = torch.zeros_like(input=x)

# Initial value of the output tensor before the first call to the model
__output1__  = m(x)

# First call to the model with modified input/output
__output2__  = m(torch.randn(64, 8))

