
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1):
        v7 = torch.matmul(x1[:, 0], 1)
        return v7
