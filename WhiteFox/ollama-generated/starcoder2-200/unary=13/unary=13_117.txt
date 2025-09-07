
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.sigmoid(v1)
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
__input_tensor__  = torch.randn(64, 784)


## Input for a new model

x1 = torch.zeros([64, 10]) # The size of this tensor is 64 x 10.
x2 = torch.zeros([64, 10], requires_grad=True) # The size of this tensor is 64 x 10 and its gradient flag is True


# A simple model using the ReLU activation function. 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t):
        return F.relu(t)

# Initializing the model with some initial weights and bias terms
m = Model()

# Feeding the model an input tensor of shape (32 x 64 x 10), with ReLU activation function
x_tensor = torch.rand(32, 64, 10)

