
class Model(torch.nn.Module):
    def __init__(self, input1dim=32):
        super().__init__()
        self.linear = torch.nn.Linear(input1dim, 50)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model