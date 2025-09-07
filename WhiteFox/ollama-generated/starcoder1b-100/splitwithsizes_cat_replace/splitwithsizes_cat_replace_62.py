
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return True  # Return True for optimization purpose (if only one torch.split and one torch.cat are used)

