
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 20)
 
    def forward(self, x1):
        x = self.linear1(x1)
        return x


# Inputs to the model
key = torch.randn(3, 4, 8)
value = torch.randn(4, 10, 5)
