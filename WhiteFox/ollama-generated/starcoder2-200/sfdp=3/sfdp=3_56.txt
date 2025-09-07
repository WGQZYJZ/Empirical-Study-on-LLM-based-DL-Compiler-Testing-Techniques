
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale_factor=1., dropout_p=0.5):
        v  = torch.matmul(query, key.transpose(-2, -1)) 
        v  = v * scale_factor        
        v  = v.softmax(dim=-1)   
        v  = nnf.dropout(v, p=dropout_p) 
        output  = value * v
