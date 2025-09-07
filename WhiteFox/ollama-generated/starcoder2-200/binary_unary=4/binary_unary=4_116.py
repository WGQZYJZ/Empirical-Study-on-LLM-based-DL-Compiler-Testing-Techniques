
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other  # Add another tensor to the result of the linear transformation
        v3  = torch.relu(v2)
        return v3


# Initializing the model with `other` passed as a keyword argument
m  = Model()
m  (torch.randn(10))

other = torch.ones_like(m.__output__)

# Inputs to the model and the additional input for the linear transformation 
x1 = torch.randn(2, 10)
__output__   = m(x1).mean()


