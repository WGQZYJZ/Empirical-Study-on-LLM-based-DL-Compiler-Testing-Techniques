
class AttentionModule(torch.nn.Module):
    def __init__(self, dim_qkv):
        super().__init__()
        self.scale = torch.sqrt(torch.FloatTensor([1] + list(dim_qkv)))
 
    def forward(self, x, q, k, v, attention_mask=None):
        # B * N * H * W -> 1 * N * B * H * W
        n, b, c = (x.shape[0], x.shape[1], x.shape[-2])
 
        # Query, Key, Value: 1 * N * B * H * W
        query, key, value = q.transpose(0, 1).contiguous().view(n, b, -1), k.contiguous().view(n, b, -1), v.contiguous().view(n, b, -1)
 
        # The scale term is used for reducing the variance of attention weights
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.scale
 
        if attention_mask:
            scaled_dot_product += attention_mask
        
        attention_weights = nn.Softmax(dim=-1)(scaled_dot_product)
 
        # Compute output tensor
        output = attention_weights.matmul(value).contiguous().view(n, b, -1)
 
        return output


# Initializing the model
m = AttentionModule([64, 64])

# Inputs to the model
q = torch.randn(8, 64, 64)
k = torch.randn(8, 64, 64)
v = torch.randn(8, 64, 64)
