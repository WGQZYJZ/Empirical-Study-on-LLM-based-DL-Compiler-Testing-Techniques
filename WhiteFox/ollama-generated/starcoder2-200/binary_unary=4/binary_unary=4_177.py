
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2)
        return v3


# Initializing the model with a keyword argument
m = Model()
other_tensor  = torch.randn(5, 8) # Other tensor to be added later in the forward pass

# Inputs for the model
x1  = torch.randn(7, 3)
__output__  = m(x1)

