
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 8)
 
    def forward(self, x2):
        v1 = self.linear(x2) # Apply a linear transformation to the input tensor
        v3 = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the linear transformation
        return v3

# Initializing model 
m = Model()

# Input tensors to the model 
x1  = torch.randn(4, 80, 20) # Size: (batch_size, num_features), the input tensor for the linear transformation
x3  = torch.randn(79, 5)     # Size: (num_features, num_classes), the input tensor to be used in the linear layer
 
 