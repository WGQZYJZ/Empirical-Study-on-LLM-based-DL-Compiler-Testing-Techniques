
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, query2, key2, value2, dropout_p=0.5, inv_scale_factor=0.5) -> None:
 
        vq  = torch.matmul(query1, key1.transpose(-2, -1))
        vq2  = qk * scale_factor # Scaling the dot product by a scalar
        vs  = vq.softmax(dim=-1) # Applying softmax to the scaled dot product
        vd  = vs * dropout_p # Multiplying by the dropout probability after applying the softmax function 
        vo  = vd.matmul(value2)
        
        return vo
