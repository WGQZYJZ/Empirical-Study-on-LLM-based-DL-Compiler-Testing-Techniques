
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
 
    def forward(self, x):
        v = self.linear(x)
        return v + other # Add another tensor to the output of the linear transformation


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(10, 16)
