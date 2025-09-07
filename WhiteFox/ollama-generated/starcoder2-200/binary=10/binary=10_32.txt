
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) + other_tensor # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model
m = Model()
 

# Inputs to the model
x1 = torch.randn(32, 25)
other_tensor = torch.randn(32, 10) # Random tensors for other_tensor should be different from __output__
