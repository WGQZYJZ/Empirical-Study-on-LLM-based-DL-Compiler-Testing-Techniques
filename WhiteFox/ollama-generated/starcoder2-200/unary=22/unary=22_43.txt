
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        v8 = torch.tanh(v7)
        return v8


# Initializing the model