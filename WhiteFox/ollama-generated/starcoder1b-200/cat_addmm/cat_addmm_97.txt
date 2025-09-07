
class Model(torch.nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.linear = torch.nn.Linear(num_features, 3)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = self.linear(x2)
        return v1 + v2


# Inputs to the model
input = torch.randn(2, 3, 4)
