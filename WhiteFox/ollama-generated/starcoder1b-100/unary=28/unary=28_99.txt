
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - min_value
        v3 = v2 / (max_value - min_value)
        return v3


# Inputs to the model
input_tensor = torch.randn(4)
