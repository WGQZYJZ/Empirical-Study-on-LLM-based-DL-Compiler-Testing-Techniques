

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        v1  = self.linear(x) # Apply a linear transformation to the input tensor
        v2 = other + v1 # Add another tensor (other is an argument of this function; do not modify it!)to the output of the linear transformation

# Initializing the model
m  = Model()

