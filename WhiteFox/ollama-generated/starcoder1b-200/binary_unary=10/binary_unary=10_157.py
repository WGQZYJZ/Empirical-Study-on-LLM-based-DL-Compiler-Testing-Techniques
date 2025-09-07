
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 10)
 
    def forward(self, x):
        v = self.linear(x) + other  # Add another tensor to the output of the linear transformation
        return relu(v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 16)
