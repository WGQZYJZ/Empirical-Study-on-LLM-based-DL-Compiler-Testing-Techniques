
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 5)
__output__   = m(x1)

