
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 7, 10)
 
    def forward(self, x1):
        x2 = x1.view(-1, 64 * 7 * 7).float()
        x3 = self.linear(x2)
        return x3


# Inputs to the model
x1 = torch.randn(20, 64, 7, 7)
