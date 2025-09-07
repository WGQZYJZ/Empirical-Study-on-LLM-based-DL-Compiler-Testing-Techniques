
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 2
        v2 = torch.relu(v1)
        return v2


# Inputs to the model
input_tensor = torch.randn(10, 15)
