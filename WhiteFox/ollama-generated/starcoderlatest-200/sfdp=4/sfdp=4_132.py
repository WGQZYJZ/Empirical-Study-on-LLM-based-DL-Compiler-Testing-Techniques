
class QueryKeyMultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
 
    def forward(self, query, key, attn_mask):
        batch_size = query.size(0)
 
        proj_query  = torch.einsum('b i d, b j n d -> b i j', [batch_size, query.shape[1], self.embed_dim, key.shape[1]])
        proj_key    = torch.einsum('b i d, b j n d -> b i j', [batch_size, key.shape[1], self.embed_dim, query.shape[1]])
 
        # Add a dimension for the number of heads
        proj_query  = proj_query.unsqueeze(-2)
        proj_key    = proj_key.unsqueeze(-3)
 
        # Compute scaled dot product between q and k (i, j): B*S x S x n x m => B*S x n x m
        attn_score = torch.matmul(proj_query, proj_key.transpose(-2, -1)) / math.sqrt(self.embed_dim)
 
        # Apply the mask for out of sequence positions
        # At this point, the attn_score has a dimension [B*S] and an additional "s" dimension. The first two dimensions must be broadcastable with each other to have a shape of [B, S], and the final one is "1". The shape of the attn_mask is determined by the input size of query (query). We use squeeze to delete the extra single-dimension of attn_mask.
        attn_score = attn_score + attn_mask  # broadcast_to(attn_score, [batch_size, -1, self.num_heads])

        # Apply softmax on the last dimension with dim=-1 to normalize it: B*S x n x m => B*S x n x m
        attn_score = F.softmax(attn_score, dim=-1)
 
        # Multiply each element of the scaled dot product by its corresponding weight vector (i, j): B*S x n x m => B*S x S x n x m
        output = torch.matmul(attn_score, proj_key)  # broadcast_to(output, [batch_size, query.shape[1], -1])
 
        # Reduce the dimension of attn_weight (i, j): B*S x S x n x m => B x S x n x m
        output = torch.einsum('b s d, b i j d -> b s i j', [output, query.shape[0], -1])
 
        # Reduce the dimension of value and key tensor (s, i): B x S x n x m => B*S x n x m
        # If you want to change the order between these two, just swap the indices of i, j in the following code. But beware that the shape of output tensor is modified as well.
        output = torch.einsum('b i s d, b s j d -> b i j', [output, query.shape[1], -2])
 
        return output

class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, embed_dim=512, num_heads=8):
        super().__init__()
        self.attn = QueryKeyMultiHeadAttention(embed_dim, num_heads)
 
    def forward(self, x):
        # Apply the multi-head attention module for each of the sequence dimensions (i and j).
        # Each sequence dimension will be transformed by a different set of weights.
        v1 = self.attn(query=x, key=x, attn_mask=torch.ones(size=(1, x.shape[1], x.shape[2])))  # Broadcast the first two dimensions for broadcastable addition later.

        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = MultiHeadSelfAttention()
 
    def forward(x):
        return self.attn(x)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
