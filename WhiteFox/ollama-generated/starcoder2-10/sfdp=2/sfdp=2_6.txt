
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.matmul(x1, key.transpose(-2,-1)) 
        v2 = v1 / 0.7071067811865476  
        v3 = torch.nn.functional.dropout(v2, p=0.9)
        