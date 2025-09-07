
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None, dropout_p=0.1):
 
        qk = torch.matmul(query / math.sqrt(query.size(-1)), torch.transpose(key, -2, -1))
        if  not attn_mask is None:
            qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = F.dropout(attn_weight, p=dropout_p)
        output = torch.matmul(attn_weight, value)
        return  output


# Initializing the model
m = Model()


