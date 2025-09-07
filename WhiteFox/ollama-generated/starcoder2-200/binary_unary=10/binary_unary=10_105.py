
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        v3 = F.relu(v2)
        return v3


# Initializing the model
m = Model()
other  = torch.randn(2048, requires_grad=True)  # Randomly initializing a tensor used as additional input

# Inputs to the model
x1  = torch.randn(256, 2048)
__output__  = m(x1)

