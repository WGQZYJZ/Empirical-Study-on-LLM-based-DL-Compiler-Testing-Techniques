
class Model(torch.nn.Module):
    def __init__(self, attn_mask=None):
        super().__init__()
 
    def forward(self, query, key, value):
        attn  = self._compute_attn(query, key)
 
        attn += attn_mask if attn_mask is not None else torch.zeros([1], device='cuda') 
        attn = torch.softmax(attn / math.sqrt(query.size(-1)), dim=-1)
        attn  = torch.dropout(attn, dropout_p=0.25, train=True)
        return query @ attn + value
 
 # Initializing the model
 m  = Model()

 # Inputs to the model
 qk = torch.randn(batch_size, 384, 196).cuda() 
 key, value  = torch.randn(batch_size, 384, 205), torch.randn(batch_size, 384, 205)

 __output__  = m(qk, key, value)

