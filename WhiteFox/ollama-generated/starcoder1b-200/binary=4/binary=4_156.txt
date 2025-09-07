
class LinearLayer(torch.nn.Module):
    def __init__(self, size=100):
        super().__init__()
        self.linear = torch.nn.Linear(size, 2)
 
    def forward(self, x):
        return self.linear(x) + other  # Add another tensor to the output of the linear transformation


# Initializing the model
l = LinearLayer()


# Inputs to the model
x1 = torch.randn(100, 3, 64, 64)
