
class TransformerModel(torch.nn.Module):
    def __init__(self, emb_dim=32, nhead=4, num_layers=6):
        super().__init__()
        self.embedding = torch.nn.Linear(emb_dim, emb_dim)
        self.norm = torch.nn.LayerNorm(emb_dim)
 
    def forward(self, src: torch.Tensor, mask: torch.Tensor):
 
        src2  = self.embedding(src) # Apply linear projection to the source token
        src3  = self.norm(src2 + src) # Add the source token with its normalized version
        src4  = torch.masked_fill(src3 - float('inf'), mask, value=float('-inf'))# Fill zeros in a tensor at specified positions
        qk = src5 @ src6.transpose(-2, -1)# Compute the dot product of the query and key (after applying dropout)
        attn_mask  = torch.tril(torch.ones(src4.size())).type(src3.dtype).to(src3.device) # Create a lower triangular matrix
        qk  += attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1)# Apply softmax to the result
        output5  = self.norm(attn_weight @ src3) # Compute the dot product of these attention weights and the source token
        return output5
 

m2  = TransformerModel()

