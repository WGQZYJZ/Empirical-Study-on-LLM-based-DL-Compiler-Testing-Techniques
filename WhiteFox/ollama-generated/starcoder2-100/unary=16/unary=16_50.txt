
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*16, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1) # Apply ReLU activation function to output of linear transformation
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(64, 32*16)

__output__  = m(x1)