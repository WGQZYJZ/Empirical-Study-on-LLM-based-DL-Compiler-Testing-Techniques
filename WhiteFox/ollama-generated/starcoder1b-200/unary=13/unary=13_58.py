
class Linear(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x1):
        return self.linear(x1).view(-1)


# Initializing the model
l = Linear()

 # Inputs to the model
x1 = torch.randn(1, 8)
