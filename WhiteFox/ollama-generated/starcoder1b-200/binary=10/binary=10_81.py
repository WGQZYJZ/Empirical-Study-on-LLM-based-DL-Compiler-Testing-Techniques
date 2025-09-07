
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 5
        return v1


# Inputs to the model
input_tensor = torch.randn(4, 2, 64, 64)
