
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.zeros_like(x1)  # Initialize a new zero tensor with the same size as the input
        return v2
 
