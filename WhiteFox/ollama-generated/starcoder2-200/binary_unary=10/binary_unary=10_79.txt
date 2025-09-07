
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 8 * 10, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying a linear transformation to the input tensor
        v2  = v1 + other      # Adding another tensor to the output of the linear transformation
        v3  = torch.relu(v2)  # Applying ReLU activation function to the result
        
        return v3

# Initializing model
m = Model()


# Inputs for the model
x1 = torch.randn(4, 3 * 8 * 10)
other = torch.randn(4, 5) # Adding another input tensor to the result of the linear transformation
__output__  = m(x1) # Running the model on inputs

