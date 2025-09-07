
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(len(x1), -1))
        v2 = v1 + v3
        v3 = torch.relu(v2)
        return v3
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(5, 64*64)
