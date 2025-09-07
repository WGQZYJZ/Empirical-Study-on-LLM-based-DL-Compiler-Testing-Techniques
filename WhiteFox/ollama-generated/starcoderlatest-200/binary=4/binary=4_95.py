
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 32)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + (other if other else torch.tensor([1])) # Add a tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
other = torch.tensor([0])
