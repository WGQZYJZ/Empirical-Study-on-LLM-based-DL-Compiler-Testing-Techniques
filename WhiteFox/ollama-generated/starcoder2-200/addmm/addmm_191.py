
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.mm(v1, 0)
        return v2

# Initializing the model with different input tensors than in previous example:
m = Model()

