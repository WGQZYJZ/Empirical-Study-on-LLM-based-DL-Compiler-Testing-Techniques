
class Attention(torch.nn.Module):
    def __init__(self, d_model, d_k):
        super().__init__()
        self.c_attn  = torch.nn.Linear(d_model, d_model)
        self.c_proj  = torch.nn.Linear(d_model, d_model)
 
    def forward(self, q, k, v):
        scores  = torch.bmm(q, k.transpose(-2,-1)) / math.sqrt(k.size(-1)) # compute the dot product of the query and key, then scale it by a scaling factor, which is sqrt(k.size(-1)), where k.size(-1) is the size of the last dimension of the key tensor
        mask = torch.zeros_like(scores).masked_fill_(attn_mask == 0, -1e9) # create an attention mask that has all values equal to 1 if the attn_mask is True, and otherwise it's equal to 1e-9. This masks out positions that should not be considered for scoring
        scores = self._masked_softmax(scores + mask)  # Apply softmax to the dot product of the scaled query and key matrices (plus a masked matrix). The resulting values are the attention weights, which will be used in the next step to compute the output.
        h  = torch.bmm(attn_weight, value)   # Compute the dot product of the dropout output and the value
        return self.c_proj(h), scores
    
    def _masked_softmax(self, q): # helper function that takes in a scaled query-key matrix (q), multiplies each row by a scalar, then applies softmax to each row separately, and returns the result
        q  = q / torch.sum(q)
        return torch.nn.Softmax(-q, dim=1)(q).clamp_(0.05, 1.)

# Initializing the model<|end_of_model|>
model = Attention(768, 64)

# Input to the model (attn is an attention mask tensor, which contains 0s and 1s; 1s in the attn_mask indicate positions where the softmax operation should be applied)<|end_of_input|>
query = torch.randn(32, 64, 768)
key   = torch.randn(32, 64, 768)
value = torch.randn(32, 64, 768)
attn_mask  = torch.ones(10, 9).masked_fill_(torch.rand(10, 9) > 0.5, 0.)

