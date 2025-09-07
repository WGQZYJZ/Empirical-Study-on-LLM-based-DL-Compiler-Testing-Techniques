
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = F.relu(v1)      # Apply the ReLU activation function to the output of the linear transformation 
        return v2
 
# Initializing the model
m  = Model() 
 
# Inputs to the model  
x1 = torch.randn(3, 64 * 64) 
