
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32768))
        v2 = torch.sigmoid(v1)
        return v2


# Inputs to the model
x1 = torch.randn(4096, 32768)
