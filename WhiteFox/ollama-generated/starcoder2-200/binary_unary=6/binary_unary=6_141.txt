
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(32, 480)
        self.lin2 = torch.nn.Linear(480, 768)
 
    def forward(self, x1):
        v1 = self.lin1(x1) 
        v2 = v1 - other
        v3 = relu(v2) 
        return v3

# Initializing the model and passing inputs to it
m  = Model()
x1 = torch.randn(4, 8, 640, 32)
y1 = m(x1)

