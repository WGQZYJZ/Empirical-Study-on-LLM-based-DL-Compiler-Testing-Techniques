
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(784, 512)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = v1 + 500 # Add another tensor to the output of linear transformation
        v3 = F.relu(v2) # Apply ReLU activation function to the output of linear transformation
        return v3

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 784)

