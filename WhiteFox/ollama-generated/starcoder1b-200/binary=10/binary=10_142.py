
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Add another tensor to the output of the linear transformation
        v2 = self.linear2(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3)
