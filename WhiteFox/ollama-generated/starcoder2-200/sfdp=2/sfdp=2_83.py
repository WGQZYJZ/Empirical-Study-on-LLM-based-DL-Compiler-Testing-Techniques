
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.functional.linear
 
    def forward(self, x1, x2):
        v3 = self.matmul(x1, x2)
        return v3


# Initializing the model