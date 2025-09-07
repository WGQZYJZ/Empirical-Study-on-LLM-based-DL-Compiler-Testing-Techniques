
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other # Add another tensor to the output of the linear transformation
        return v6


# Initializing the model
m = Model()
m.other = torch.randn(10, 4)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
