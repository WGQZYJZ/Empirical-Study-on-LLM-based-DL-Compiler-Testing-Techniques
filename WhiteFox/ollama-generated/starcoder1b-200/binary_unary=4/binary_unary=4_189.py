
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn(10, 20, dtype=torch.float32) * 0.5
        return relu(v1)


# Initializing the model
m = Model()

