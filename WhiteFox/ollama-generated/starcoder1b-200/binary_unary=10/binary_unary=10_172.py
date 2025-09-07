
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn(v1.size())  # Add a random tensor to the output of the linear transformation
        return relu(v2)


# Inputs to the model
x1 = torch.randn(1, 32 * 32)
