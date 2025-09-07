
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v1 + other


# Inputs to the model
x1 = torch.randn(200, 3) # Input tensor with shape (N, D) where N is the batch size and D is the number of input dimensions
