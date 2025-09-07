
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*16, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.relu(v1) # A common pattern in many neural network architectures, where a linear transformation is followed by a non-linear activation function.
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10, 32*16) # Please generate a different input tensor than x1 of the previous question.
__output__  = m(x1)

# Questions

## Question 1
