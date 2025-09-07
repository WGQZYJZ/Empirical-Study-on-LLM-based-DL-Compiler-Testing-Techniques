
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32 * 64, 500)
        self.linear2 = torch.nn.Linear(500, 700)
 
    def forward(self, x1):
        v1 = self.linear1(x1.view(-1, 32 * 64))
        v2 = torch.sigmoid(v1)
        v3 = self.linear2(v2)
        v4 = torch.tanh(v3)
        v5 = v4 + 1
        v6 = v2  * v5
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 