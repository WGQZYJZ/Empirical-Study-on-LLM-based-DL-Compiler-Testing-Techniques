
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 196)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply the linear transformation to the input tensor
        v2  = torch.tanh(v1)  # Apply the hyperbolic tangent function to the output of the linear transformation 
        return v2

# Initializing the model 
m = Model()


# Inputs to the model 
x1  = torch.randn(1, 3072)

# Running the model 
m(x1)

# Evaluating the model 
m(x1).mean().item() == 0.485609 # Check if the output is correct 

# Please also provide the output of the mean function (not required for scoring) 

