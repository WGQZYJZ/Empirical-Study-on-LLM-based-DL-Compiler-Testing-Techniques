
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor
        return v2

# Initializing the model and getting a sample input tensor
m  = Model()
x1 = torch.randn(30, 3)

