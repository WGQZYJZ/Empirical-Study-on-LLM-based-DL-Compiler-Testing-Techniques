
class LinearLayer(torch.nn.Module):
    def __init__(self, n1, n2):
        super().__init__()
        self.fc1 = torch.nn.Linear(n1, n2)
 
    def forward(self, x1, other):
        v1  = self.fc1(x1)
        return v1 + other

# Initializing the model
layer = LinearLayer(3, 4)

