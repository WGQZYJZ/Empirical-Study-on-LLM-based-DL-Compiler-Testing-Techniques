
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 2  # Subtract 2 from the output of the linear transformation
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
inputs = [[1.0], [10.0], [999.0]]
outputs = [0.0, -100.0, 998.0]
