
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8192, 50)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v3  = v1 + other_tensor
