
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(256, 3)
 
    def forward(self, x1, x2=None):
        v1 = self.m(x1)  # Use the first linear layer of the model to process the input tensor 'x1'
        if x2 is None:  # If no input is given
            inp = torch.randn(32, 500)   # Generate random tensor 'inp'
            v2 = self.m(inp)        # Apply the second linear layer of the model to generate output from 'inp'
        else:                           # Otherwise if an input is given
            v2 = self.m(x2)         # Apply the second linear layer of the model to process the input tensor 'x2'
        return v1 + v2


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor1  = torch.randn(256, 300)   # Generate random tensor with 300 values between -1 and 1
input_tensor2 = torch.randn(10, 300)   # Generate random tensor with 300 values between -1 and 1
