
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + other_tensor #other tensor is randomly generated and has shape (8,)
        v3  = F.relu(v2) # The ReLU activation function
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 1024) 

# Initialization of a random tensor
other_tensor = torch.randn((8))

# The initialization of the output variable is not necessary for scoring, but we need it to create a valid PyTorch model with public PyTorch APIs that meets the specified requirements
__output__   = m(x1)

