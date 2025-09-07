
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other # Add another tensor to the output of the linear transformation
        return v1


# Inputs to the model
x1  = torch.randn(1, 5)
other  = torch.randn(1, 3)
