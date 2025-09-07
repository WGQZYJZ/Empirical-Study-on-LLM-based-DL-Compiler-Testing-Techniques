
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        v1  = torch.matmul(query1, key1.transpose(-2, -1))
        v2  = v1.div(5)
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.987654321)
        v5  = v4.matmul(value1)
