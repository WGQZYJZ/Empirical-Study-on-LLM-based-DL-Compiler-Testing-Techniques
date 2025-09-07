
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.where(v1 > 0, v1, v1 * -0.0001) # Leaky ReLU function
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
