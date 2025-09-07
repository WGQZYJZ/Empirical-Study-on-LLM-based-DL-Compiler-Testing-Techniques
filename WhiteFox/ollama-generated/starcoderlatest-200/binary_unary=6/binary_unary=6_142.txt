
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1.9841278253786532e-03 # subtracting the constant 'other' from the output of linear transformation
        v3 = torch.nn.functional.relu(v2) # applying the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 1024, 8, 64)
