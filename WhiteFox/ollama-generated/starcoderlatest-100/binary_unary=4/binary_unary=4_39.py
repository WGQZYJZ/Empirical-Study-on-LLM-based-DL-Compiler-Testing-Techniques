
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model(torch.randn(1, 4))

# Inputs to the model
x1 = torch.randn(1, 8)
