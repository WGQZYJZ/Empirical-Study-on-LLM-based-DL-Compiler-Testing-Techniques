
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1) # apply a linear transformation to the input tensor
        v2 = v1 + other # add another tensor to the output of the linear transformation 
        v3 = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing the model