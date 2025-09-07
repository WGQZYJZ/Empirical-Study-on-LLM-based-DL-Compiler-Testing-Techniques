
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 1, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1).reshape((len(x1), -1))
        v2 = F.sigmoid(v1)
        v3 = v2 * v1
        return v3


# Initializing the model