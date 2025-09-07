
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 32, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Linear transformation
        v2 = v1 - other   # Subtract 'other' from the linear output
        v3 = F.relu(v2)    # Apply ReLU to the linear output 
        return v3


# Initializing the model 
m = Model()

# Inputs to the model
x1 = torch.randn(4, 128)
__output__  = m(x1)

