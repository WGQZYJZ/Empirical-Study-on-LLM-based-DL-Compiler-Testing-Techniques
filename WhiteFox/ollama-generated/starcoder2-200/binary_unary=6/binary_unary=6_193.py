
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.tensor([2])
        v1  = self.linear(x1) - v0[0] 
        v2 = F.relu(v1) # Apply the ReLU activation function to 'v1'
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 84)

__output__  = m(x1)

