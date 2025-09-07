
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other_value # Subtract 'other' from the output of the linear transformation
        v3  = F.relu(v2)  # Apply the ReLU activation function to the result
        return v3
# Initializing the model with input 2D tensor, and initialize the parameters 
other_value  = torch.randn((10),dtype=torch.float32)
 
m2 = Model2()

