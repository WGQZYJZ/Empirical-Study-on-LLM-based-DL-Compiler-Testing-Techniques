
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Add another tensor to the output of the linear transformation
        v2 = relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(10, 10)
