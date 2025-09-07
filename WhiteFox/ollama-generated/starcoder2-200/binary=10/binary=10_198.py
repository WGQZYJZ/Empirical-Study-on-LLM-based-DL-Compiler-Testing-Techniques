
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + x # Add another tensor to the output of the linear transformation
        return v2


# Initializing and using the model