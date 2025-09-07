
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.layer = torch.nn.Linear(8, 1)
 
    def forward(self, x1):

        v0 = torch.relu(x1)
        return torch.softmax(v0)

# Initializing the model