
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 7
        return v1


# Initializing the model