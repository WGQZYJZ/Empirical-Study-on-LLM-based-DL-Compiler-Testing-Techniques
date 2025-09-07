
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10 * 3, 8)
 
    def forward(self, x1): 
        v1 = self.fc(x1) # Apply a linear transformation to the input tensor
        v2 = torch.nn.functional.relu(v1)# Apply ReLU activation function to output of the linear transformation
        return v2


# Initializing the model 
m_2  = Model2()
 
# Inputs for the model
x1 = torch.randn(10,3) 

# Executing the model with inputs 
__output___ = m_2(x1)
