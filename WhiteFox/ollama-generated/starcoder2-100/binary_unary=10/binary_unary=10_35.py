
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(4096, 2)(x1) # Apply a linear transformation to the input tensor 
        v2 = v1 + other_tensor()          # Add another tensor to the output of the linear transformation  
        v3 = torch.relu(v2)                # Apply the ReLU activation function to the result  
        return v3

# Initializing the model 
m = Model()

 # Inputs to the model  
x1 = torch.randn(64, 4096) 
 
