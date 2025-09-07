
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2):
        v1  = torch.matmul(query1, key2.transpose(-2, -1)) 
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = dropout_p > 0
        v5  = torch.nn.functional.dropout(v3, p=dropout_p) if v4 else v3
        v6  = v5.matmul(value) 
        return v6

m = Model()
 
q1  = torch.randn(2, 80, 768)
k2  = torch.randn(2, 768, 768)  # In practice the size of this tensor is usually larger than that of the value tensor in the above pattern
__output__  = m(q1, k2)

