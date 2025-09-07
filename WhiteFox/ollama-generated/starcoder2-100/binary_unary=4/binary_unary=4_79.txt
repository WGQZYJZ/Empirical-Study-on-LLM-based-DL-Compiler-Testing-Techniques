
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(30, 8)(x1)
        v2  = v1 + torch.randn_like(v1)
        v3  = F.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 30)

__output__  = m(x1)