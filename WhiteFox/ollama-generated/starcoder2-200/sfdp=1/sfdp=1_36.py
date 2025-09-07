
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(0.1)
        self.dropout = torch.nn.Dropout()
    
    def forward(self, xq, xt):
        k, v = torch.meshgrid((xq,), (xt,))
        qk  = torch.matmul(kq[...,:], kt[..., None]).div_(self.scale) # Compute the dot product of the query and key tensors
        sk  = qk.softmax(dim=-1).unsqueeze(-2)                         # Apply softmax to the scaled dot product
        output_values  = torch.einsum("ib, ab, jb -> ia", sk, v)       # Compute the dot product of the dropout output and the value tensor 
        return self.dropout(output)
