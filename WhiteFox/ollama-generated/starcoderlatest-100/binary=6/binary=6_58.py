
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 1)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()
other = torch.tensor([[-0.3]]) # input tensor for the linear transformation

# Inputs to the model
x1 = torch.randn(1, 64, 64)
