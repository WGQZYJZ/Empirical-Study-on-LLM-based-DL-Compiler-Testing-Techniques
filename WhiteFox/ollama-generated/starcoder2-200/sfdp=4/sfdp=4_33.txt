
class MultiHeadedAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8):
        super().__init__()
        assert (embed_dim % num_heads == 0), 'embedding dim must be divisible by the number of heads'
 
        self.num_heads = num_heads

        # Embedding layer
        self.input_linearity = torch.nn.Linear(embed_dim, embed_dim)
        self.output_linearity = torch.nn.Linear(embed_dim, embed_dim)
 
        # Scaled dot-product attention: Compute the dot product of the query and key tensors, and scale it with a scaling factor
        # Add the scaled dot-product attention to the original embedding dimension in order to produce the new embedding vector
        self.scaled_attention = ScaledDotProductAttention(embed_dim=embed_dim)
 
        self.layernorm1 = torch.nn.LayerNorm(embed_dim, eps=1e-06)

    def forward(self, query):
        batch_size = query.shape[0]

        # Embedding layer to produce the embedding vectors for each token
        h  = self.input_linearity(query)

        # Apply layer normalization on the embedding vectors produced by the embedding layers
        # Concatenate all the heads into one tensor with shape (num_heads, batch size, sequence length of a head, embedding dimension per head)
        h = h.reshape((batch_size * self.num_heads,) + h.shape[-2:])

        # Apply scaled dot-product attention on each head: Compute the dot product of the query and key tensors for each head in the batch, and scale it with a scaling factor
        # Concatenate all the heads back into one tensor after applying softmax to the results
        attn_weights = self.scaled_attention(h)[0]
 
        # Apply layer normalization on the embedding vectors produced by the attention head
        # Re-reshape the new embedding vector back into a 3D tensor with shape (batch size, sequence length of a head, embedding dimension per head)
        # Pass this reshaped 3D tensors to a feedforward network
        h = self.layernorm1(h @ attn_weights).view((batch_size,) + h.shape[-2:])

        # Apply linearity to the output tensor produced by the feed-forward network
        return self.output_linearity(h)


