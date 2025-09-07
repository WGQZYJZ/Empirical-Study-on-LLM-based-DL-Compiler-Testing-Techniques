
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.5 # Apply a linear transformation to the input tensor
        v3 = F.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()

