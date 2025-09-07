
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query,key.transpose(-2,-1))
        v2  = v1 / math.sqrt(scale)
        v3  = torch.nn.functional.dropout(v2, p=dropout_prob) #p=dropout_prob
        return v3.matmul(value)
