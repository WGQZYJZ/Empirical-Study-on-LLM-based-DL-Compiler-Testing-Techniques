
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, dim=64, embed_dim=128):
        super().__init__()
        self.embed = torch.nn.EmbeddingBag(embed_dim, num_heads * embed_dim)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        q  = x1.clone() # qk matrix of the input tensor and shape (batch_size, seq_length, num_heads * dim)
        k  = self.embed(x1).transpose(1, 2).contiguous().view(-1, q.shape[-1])
        v  = self.embed(q).contiguous().view(-1, k.shape[-1]) # shape (batch_size * seq_length, num_heads * dim)

        # Compute the dot product of the query and key matrix and scale it
        qk = torch.einsum('bhdk,bhdh->bhkd', q, k) / math.sqrt(k.shape[-1]) # shape (batch_size, seq_length, num_heads * dim)

        # Add an attention mask to the scaled dot product
        attn_mask = (q @ k).gt(0)  # A mask for selecting only valid inputs by the attention algorithm
        attn_mask = attn_mask.unsqueeze(2).expand_as(qk)  # expand attention mask to the right shape

        # Compute the softmax over all heads of attention weights
        attn_weight = torch.softmax(qk, dim=-1)

        # Dropout the computed attention weights
        attn_weight = torch.dropout(attn_weight, dropout_p, True) 
        
        # Compute the dot product of the dropout weight matrix and the value vector
        output = attn_weight @ v
        return output


# Initializing the model
m = Model()

