
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 1024)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, x1.size(1)*x1.size(2)*x1.size(3)))
        v2 = torch.tanh(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 64*64)
