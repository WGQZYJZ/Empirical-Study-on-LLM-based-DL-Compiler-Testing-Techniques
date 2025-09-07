
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
 
        # We assume that all dimensions except the second dimension have the same size in input and output
        self.query_proj  = torch.nn.Linear(768, self.num_heads * 64)
        self.key_proj    = torch.nn.Linear(768, self.num_heads * 64)
        self.value_proj  = torch.nn.Linear(768, self.num_heads * 64)
 
        # These lines define how many dimensions the input and output of linear transformation has
        self.scale = math.sqrt(1 / (2 * num_heads))
 
    def forward(self, query, key, value):
        batch_size = query.shape[0]
 
        # In this example, we set d_k to equal d_v, but it can be different from the input and output dimensions if needed
        d_k = query.shape[-1]
 
        # We reshape the query tensor because linear transformation only supports tensors with 3 or more dimensions
        qk  = self.query_proj(query).view(-1, batch_size, self.num_heads, d_k)
        vk  = self.key_proj(key).view(-1, batch_size, self.num_heads, d_k)
        vv  = self.value_proj(value).view(-1, batch_size, self.num_heads, d_k)
 
        # Attention is computed as a dot product between query and key vectors (qk), followed by a scale and softmax function
        scaled_qk = qk * self.scale
 
        attn  = scaled_qk.matmul(vk.transpose(-2, -1))
        # Softmax and dropout are applied on the attention map of size: B x N x L X d_k -> B x N x L x L

        softmax_attn = torch.nn.functional.softmax(attn, dim=-1)
        dropout_attn = torch.nn.functional.dropout(softmax_attn, p=0.5)
 
        output = (dropout_attn).matmul(vv)  # Softmax is applied on the attention map of size: B x N x L X d_v -> B x N x L x d_k
        # This result is then used to compute a matrix multiply between self-attention and concatenation

        return output.view(-1, batch_size, output.shape[-2], query.shape[-1])
 
# Initializing the model
m = MultiHeadAttention(num_heads=8)


# Inputs to the model
x1 = torch.randn(2, 768, 56, 56)
