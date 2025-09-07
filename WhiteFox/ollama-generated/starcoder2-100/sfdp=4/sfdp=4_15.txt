
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        v1  = torch.matmul(query,key.transpose(-2,-1))/math.sqrt(query.size(-1))
        if not None == v1:
            v1  += attn_mask
        attn_weight = torch.softmax(v1)
        output  = torch.matmul(attn_weight, value)
        return output


m  = Model()


query  = torch.randn(2,56)
key   = torch.randn(2,7394, 56)
value = torch.randn(2,180,512)
__output__  = m(query, key, value)

