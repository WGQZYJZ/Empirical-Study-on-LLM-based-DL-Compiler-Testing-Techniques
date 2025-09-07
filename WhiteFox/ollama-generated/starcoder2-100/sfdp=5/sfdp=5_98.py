
class Attention(torch.nn.Module):
    def __init__(self, n_head=128, dropout_p=0.3):
        super().__init__()
 
        self.n_head = n_head  # the number of heads in multi-headed self-attention
        self.dmodel = dmodel  # the input embedding size
 
        self.qkv_linear = torch.nn.Linear(self.dmodel, self.n_head * (2*3 + 1)) 
        self.output_linear  = torch.nn.Linear(self.n_head, self.dmodel)
 
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, query, key=None, value=None):
        # Scaled dot-product attention 
        qkv = self.qkv_linear(query)  # [N*T1,n_head*3, D_model]
        if key is not None:
            attn_mask = torch.einsum('ijk->jik',  qkv_pad)  # [N*T1-T2,n_head*3, T2]
 
        q, k, v = torch.chunk(qkv, 3, dim=2) 
        qk = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.dmodel) 
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)
        attn_weight = self.dropout(attn_weight)  # [N*T1-T2,n_head, T2]
 
        output = torch.matmul(attn_weight, v)  # [N*T1-T2, n_head, Dmodel]
        output = self.output_linear(output) 
        return output


# Initializing the model
a = Attention()


