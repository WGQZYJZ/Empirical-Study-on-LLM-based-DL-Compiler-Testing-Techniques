
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3*64**2, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = F.relu(v1)
        return v2


# Initializing the model