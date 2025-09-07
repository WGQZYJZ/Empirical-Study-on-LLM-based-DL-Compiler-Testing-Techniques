
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn(1024)  # Add the result of the linear transformation to another tensor
        v2 = self.relu(v1)                       # Apply the ReLU activation function
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 1, 64, 64)
