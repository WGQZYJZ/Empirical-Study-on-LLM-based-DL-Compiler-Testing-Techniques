
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 512)
        self.key = torch.nn.Linear(1024, 512)
 
    def forward(self, q, k, v, attn_mask):
        v_shape = list(v.size()) # Store the dimensions of the value tensor
        batch_size = int(v.shape[0]) # The shape of `k` is (batch_size, num_heads, embed_dim // num_heads) and `attn_weight` is (batch_size, num_heads, 1, key_length, query_length), therefore the dimension of q must be equal to the value tensor except batch size.
        v = self.query(v).view(v_shape[0], -1, int(v.shape[2] / int(v.shape[1]))) # The shape of `q` is (batch_size, embed_dim) and the output dimension of self.query is (embed_dim, 512), therefore we can reshape it to (embed_dim // num_heads, -1).
        q = self.key(q).view(-1, int(v.shape[1]), 1).expand(batch_size, int(v.shape[1]), q.shape[-1]) # The shape of `k` is (batch_size, embed_dim) and the output dimension of self.key is (embed_dim // num_heads, -1), therefore we can reshape it to (batch_size, embed_dim // num_heads, -1).
        qk = torch.einsum('bhld,bhljd->bhld', q, k)  # The shape of `qk` is (batch_size, embed_dim // num_heads, query_length, key_length).

        attn_weight = torch.softmax(qk / math.sqrt(int(v.shape[1])), dim=-1)  # The shape of `attn_weight` is (batch_size, embed_dim // num_heads, query_length, key_length), and we can use softmax operation to normalize the scaled dot product of the attention query vector with each key vector in the value tensor.
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # The shape of `attn_weight` is (batch_size, embed_dim // num_heads, query_length, key_length), and we can use dropout operation to mitigate the risk of overfitting during training.

        output = torch.einsum('bhlid,bhld->bhljd', attn_weight, v)  # The shape of `output` is (batch_size, embed_dim // num_heads, query_length, key_length), and we can use einsum operation to multiply the attention weights with the value tensor.
        output = output.view(v_shape[0], -1, v_shape[2]) # The shape of `output` is (batch_size, embed_dim // num_heads * query_length, key_length), and we can use view to reshape it into a Tensor with the dimensions specified by the shape variables.
        return output


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(1, 3072, 64) # (batch_size, embed_dim, num_heads, query_length)
k = torch.randn(1, 3072, 512) # (batch_size, embed_dim, num_heads, key_length)
v = torch.randn(1, 1024, 512) # (batch_size, embed_dim, num_heads, value_length)
attn_mask = torch.ones((1, 3072, 64)) # (batch_size, embed_dim, num_heads, query_length, key_length)
