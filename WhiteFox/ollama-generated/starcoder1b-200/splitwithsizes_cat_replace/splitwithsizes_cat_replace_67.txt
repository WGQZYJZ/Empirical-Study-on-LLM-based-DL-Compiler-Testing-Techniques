
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.cat([x1, x2, x3])  # No need to do anything with the two inputs here

