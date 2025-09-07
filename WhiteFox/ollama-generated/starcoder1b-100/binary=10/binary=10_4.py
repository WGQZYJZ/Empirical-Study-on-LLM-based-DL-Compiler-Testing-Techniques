
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3
        return v1


# Inputs to the model
inputs = [torch.randn(5, 10), torch.randn(5, 20)]
