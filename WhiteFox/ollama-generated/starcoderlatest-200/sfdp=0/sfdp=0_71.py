
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        q = torch.matmul(x1, x2.transpose(-2,-1)) / math.sqrt(x1.shape[1])
        return q
