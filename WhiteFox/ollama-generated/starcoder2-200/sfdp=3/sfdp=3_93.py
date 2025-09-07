
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.tensor([0.2], dtype=torch.float32)
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2.transpose(-2, -1)) 
        v2  = v1 * self.scale 
        v3  = v2.softmax(dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.75)
        return v4
