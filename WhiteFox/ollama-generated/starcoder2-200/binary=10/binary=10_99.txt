
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other_tensor # Add another tensor (specified by keyword argument "other") 
        return v2


# Initializing model and setting "other" value
m  = Model()
m.eval()
other_tensor = torch.randn(8, 3)
m(x1)

# Input to the model is set
x1 = torch.randn(10, 32)


