
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3072)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor  # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3072, 100)
