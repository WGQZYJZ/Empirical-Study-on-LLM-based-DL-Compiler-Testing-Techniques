
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        return l5

 # Inputs to the model
x1 = torch.randn(1, 3, 42, 42)
