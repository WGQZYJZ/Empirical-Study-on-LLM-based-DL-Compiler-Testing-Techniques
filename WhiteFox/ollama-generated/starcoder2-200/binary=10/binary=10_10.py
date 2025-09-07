
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        return v1 + torch.randn(v1.size())


# Initializing the model and getting input tensor