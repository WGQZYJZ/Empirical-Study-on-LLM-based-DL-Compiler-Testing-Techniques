
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1) # linear transformation
        v2 = v1 - other_value
        v3 = F.relu(v2)  # ReLU activation function is applied to the result of 'other' value being subtracted from the linear transformation
        return v3

# Initializing model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 64)
__output__  = m(x1)