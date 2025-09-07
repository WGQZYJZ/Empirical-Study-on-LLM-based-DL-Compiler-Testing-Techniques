
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        inv_scale = torch.tensor([0])
 
        v1  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale 
        v4 = torch.nn.functional.dropout(v1.softmax(dim=-1), p=0)
        v5  = v4 @ value
 
        return v5
