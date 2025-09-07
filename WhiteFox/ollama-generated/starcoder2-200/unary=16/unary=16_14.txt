
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying linear transformation on the input tensor 
        v2  = torch.nn.functional.relu(v1) # Apply ReLU to the output of the linear transformation.
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32, 256)
__output__  = m(x1)

