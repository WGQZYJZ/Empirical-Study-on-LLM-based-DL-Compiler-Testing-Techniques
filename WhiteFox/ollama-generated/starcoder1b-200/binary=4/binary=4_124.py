
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 0.1
        return v1


# Inputs to the model
input_tensor = torch.randn(1, 2, 4)
