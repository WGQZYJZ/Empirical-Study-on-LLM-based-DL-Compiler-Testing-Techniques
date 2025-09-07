
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(3 * 64 * 64, 512)
 
    def forward(self, x1):
        v1 = self.l1(x1.view(x1.shape[0], -1))
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
