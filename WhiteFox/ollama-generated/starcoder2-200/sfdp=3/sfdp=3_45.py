
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
         v1  = torch.matmul(x1, self.linear.weight) # Compute the dot product of the query and key tensors
         v2  = v1.mul(0.75)                           # Scale the dot product by a factor
         v3  = torch.nn.functional.relu(v2)           # Apply relu to the scaled dot product
         return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(8, 3, requires_grad=True)
 
 # Predicted output
