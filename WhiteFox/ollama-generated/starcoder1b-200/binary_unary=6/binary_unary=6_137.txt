
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - 5) * 2
        v3 = relu(v2)
        return v3


# Inputs to the model
input_tensor = torch.randn(1, 4, 64, 64)
