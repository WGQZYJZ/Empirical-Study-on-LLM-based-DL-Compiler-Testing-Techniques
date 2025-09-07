
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.q = torch.nn.Linear(d_model, d_k)
        self.v = torch.nn.Linear(d_model, d_v)
 
    def forward(self, k, v, q, mask=None):
        # Apply linear projections
        k = self.q(k)
        v = self.v(v)
 
        # Convert query and key to contiguous, apply attention on the non-masked positions
        scores = torch.einsum('bhld,bhmd->bhlmd', q, k)
        if mask is not None:
            scores.masked_fill_(mask, float('-inf'))
        p_attn = F.softmax(scores, dim=-1)
 
        # Apply attention on the non-masked positions
        context = torch.einsum('bhlmd,bhmd->bhld', p_attn, v)
 
        return context, p_attn
