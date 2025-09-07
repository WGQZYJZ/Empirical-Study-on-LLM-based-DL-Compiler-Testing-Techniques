
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(832, 1024)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = relu(v2) # Add a ReLU activation function to the result of subtracting 'other' from the output
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 832)
other = x1 * 0 + 549755813888 # This value may be different each time a model is generated
