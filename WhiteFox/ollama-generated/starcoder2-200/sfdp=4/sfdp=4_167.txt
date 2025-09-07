
class Attention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.embed_dim = embed_dim
        self.qkv  = torch.nn.Linear(self.embed_dim , 3 * embed_dim)
 
    def forward(self, input_, key=None, value=None, mask=None):
        qk = self.qkv(input_)
 
        query  = qk[:, :embed_dim] / math.sqrt(qk.size(-1))
        key = query if key is None else key
        value = query if value is None else value
        attn_mask = torch.zeros([1, ] * len(query.shape) + [key.shape[-2], key.shape[-2]])
        return qk  @ key.transpose(-2,-1).softmax(-1) @ value
 
