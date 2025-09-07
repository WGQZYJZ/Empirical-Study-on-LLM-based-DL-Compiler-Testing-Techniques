
class MultiHeadAttention(nn.Module):
    def __init__(self, embeds_dim: int = 768,
                 head_num: int = 12) -> None:
        super().__init__()
        self._embeds_dim = embeds_dim
        self._head_num = head_num

        assert (embeds_dim % head_num == 0), \
            "embeds dim ({}) should be divided by the number of heads ({}).".format(
                embeds_dim,
                head_num)
        
        self.k_proj = nn.Linear(self._embeds_dim,
                                self._embeds_dim)
        self.q_proj = nn.Linear(self._embeds_dim,
                                self._embeds_dim) 
        self.v_proj = nn.Linear(self._embeds_dim,
                                self._embeds_dim)
    
        self.o_proj = nn.Linear(self._embeds_dim,
                                self._embeds_dim)
 
    def forward(self, query: Tensor,
                key: Optional[Tensor]  = None, 
                value: Optional[Tensor] = None):
        q = self.q_proj(query).view(*query.shape[:-1],
                                     -1, # n_head
                                     self._embeds_dim)
    
        k = self.k_proj(key).view(*key.shape[:-2],
                                   -1, 
                                   self._embeds_dim)
        v = self.v_proj(value).view(*value.shape[:-2],
                                      -1, 
                                      self._embeds_dim)

        if key is None:
            k = q
        if value is None:
            v = k
 
        attn_mask = query.new_ones(q.shape[0])
        attn_weight = torch.bmm(q,
                                 k.transpose(-1,-2)) / math.sqrt(self._embeds_dim) + attn_mask.unsqueeze(1).unsqueeze(3)
        attn_weight = F.softmax(attn_weight,
                                dim=-1) # batch,head,len,len
    
        attn_output  = torch.bmm(attn_weight,
                                 v)  # batch,head,len,dim
 
        attn_output = attn_output.view(*query.shape[:-2],
                                       -1,# head 
                                       self._embeds_dim
                                      )
 
        output = self.o_proj(attn_output).view(
            *query.shape[:-1] + (-1,))

        return output

