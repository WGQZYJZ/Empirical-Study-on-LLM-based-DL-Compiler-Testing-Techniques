
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other_tensor
        return v2


# Initializing the model with randomly generated tensors as inputs and a keyword argument 'other' in the linear function: 
m  = Model()
other_tensor  = torch.randn(1, 4)

# Inputs to the model
x1  = torch.randn(1, 100)


