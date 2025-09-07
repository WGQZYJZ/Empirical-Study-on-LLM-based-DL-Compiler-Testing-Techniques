
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3*64*64, 8)
 
    def forward(self, x1):
        v0 = self.conv(x1) # Apply linear transformation to input tensor
        v1 = F.relu(v0)  # Apply the ReLU activation function to output of linear transformation
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3*64*64)
__output__  = m(x1)

