
class SelfAttention(torch.nn.Module):
    def __init__(self, d_model=512, num_heads=8, dropout=0.1):
        super().__init__()
 
        # TODO: define and initialize layer norm, query projection and key value projection
        self.norm  = torch.nn.LayerNorm(d_model)
        self.qkvproj = torch.nn.Linear(d_model, d_model * 3, bias=False)
 
    def forward(self, x):
 
        # TODO: define the main part of the self-attention mechanism, where the query projection, scaling and softmax is done
        qk, v  = self.qkvproj(x).chunk(3, dim=-1)
        qk_t  = qk @ torch.softmax(qk / math.sqrt(x.size(-1)), -2)
        # Apply dropout to the softmax output 
        k  = torch.dropout(self.attn(x), dropout, True)
        # Compute the dot product of these attention weights and the value 
        return self.norm(self.output(x))
 
 
m = SelfAttention()


Inputs to the model