
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        v3 = torch.nn.functional.relu(v2)
        return v3
# Initializing the model
m = Model()


# Inputs to the model
other  = torch.randn(4, 3, 64, 64)
x1 = torch.randn(1, 32, 64, 64)
