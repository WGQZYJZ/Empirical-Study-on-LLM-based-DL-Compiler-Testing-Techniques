
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64000, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply the linear transformation to the input tensor
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
inputs = torch.randn(567890, 423000)
