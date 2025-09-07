
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(3 * 64 * 64, 50)
 
    def forward(self, x1):
        v1 = self.l1(x1.view(x1.size(0), -1))
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64 * 64 * 3)
