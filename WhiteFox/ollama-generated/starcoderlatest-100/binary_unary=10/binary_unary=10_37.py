
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 1024, 7, 7) # input_tensor is the size (1, 1024, 64, 64)
x2 = torch.randn(1, 5, 8, 8) # other is the size (1, 5, 8, 8)
