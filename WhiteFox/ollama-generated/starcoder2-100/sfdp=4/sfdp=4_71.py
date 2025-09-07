
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head=8):
        super().__init__()
 
        self.n_head  = n_head # Number of heads for the transformer model
        self.dim  = 768  # Dimensions of hidden layers
        self.query  = torch.nn.Linear(self.dim, self.dim) 
        self.key   = torch.nn.Linear(self.dim, self.dim) 
        self.value  = torch.nn.Linear(self.dim, self.dim) 
 
        self.dropout  = torch.nn.Dropout(0.1) # Dropout probability
 
    def forward(self, query):
 
        query = query + torch.randn_like(query).uniform_(
            -1e-6, 1e-5
        ) # Apply random Gaussian noise to the input tensor
        batchsize, length = query.shape[:-2], query.shape[-2:] 
        assert self.dim % self.n_head == 0
        n = int(self.dim / self.n_head)
 
        # Apply a dot product followed by a softmax to compute attention weights
        scaled = (
            torch.einsum("...d,...dh->...hd", query, self.key(query)) * 1e-5
        ) # Multiply the input tensor by 0.000001
        attn_mask = torch.ones(*batchsize[:-2], length[0],
                                length[-1]) # Generate a mask that contains ones for all positions in the sequence
 
         # Apply the attention mask to the scaled dot product
        attn_weight  = self._compute_attention(scaled, length)
 
        # Compute the weighted average of the value tensor based on the attention weights and then apply dropout to this result
        output = torch.einsum("...hd,...dv->...v",
                              attn_weight, self.value(query)) 
        output = self.dropout(output)
 
        return output
 
    def _compute_attention(self, scaled, length):
         # Compute the dot product of the query and key tensors and scale them
        qk  = torch.einsum("...d,...dh->...hd", scaled,
                            self.key(scaled)) / math.sqrt(scaled.size(-1)) 
        qk  = qk + attn_mask 
 
         # Apply softmax to the dot product of the query and key tensors
        attn_weight  = torch.softmax(qk, dim=-2)
        return attn_weight
 
 
# Initializing the model with the number of heads set to 8
model  = MultiHeadAttention(n_head=8)


__output__  = model(torch.randn(10, 32))