
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.layer = torch.nn.Linear(256, 3)
 
    def forward(self, x1):
        v1 = layer(x1) # Apply the linear transformation to an input tensor. 
        v2 = F.relu(v1) # Apply the ReLU activation function to the output of the linear transformation.
        return v2

# Initializing the model