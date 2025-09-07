
class Model(torch.nn.Module):
    def __init__(self, qk_dim, v_dim, dpr=1.0):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim_q=qk_dim, dim_k=qk_dim, dim_v=qk_dim, num_heads=1)
        # Use a learned positional embedding for the key and query to save memory when the model is used on short sentences
        self.attn_pos = torch.nn.Linear(v_dim, qk_dim * 2, bias=False)
 
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 3, 1).contiguous().view(x1.shape[0], -1, x1.shape[-1])
        v2 = x2.permute(0, 2, 3, 1).contiguous().view(x2.shape[0], -1, x2.shape[-1])
        key_len, query_len = x1.size(-2), x2.size(-2)
        qk_dim, v_dim = self.attn.dim_q, self.attn.dim_v
        # Embed the positional tokens in a learned manner to save memory
        v1 = self.attn_pos(v1).view(-1, query_len, qk_dim * 2)
        v2 = self.attn_pos(v2).view(-1, key_len, qk_dim * 2)
        scaled_qk = self.attn(v1, v2, v2)[0]
        # Use a learned positional embedding to save memory in the softmax computation of the attention mechanism
        attention_weights = scaled_qk.div(np.power(v1.shape[-1], 0.5)).permute(0, 2, 3, 1)
        # Apply dropout before computing softmax and softmax scaling to prevent overfitting
        attention_weights = torch.nn.functional.dropout(attention_weights, p=dpr)
        attention_weights = scaled_qk / np.power(v1.shape[-1], 0.5).permute(0, 2, 3, 1)
        # Compute softmax over the last dimension and apply dropout before computing dot product between query and key to save memory
        attention_weights = torch.nn.functional.dropout(attention_weights, p=dpr)
        # Apply dot product attention with learned positional embeddings for queries and keys to compute query-key attention weights
        attention_context = self.attn(x1, x2, attention_weights)[0]
        attention_context = attention_context.view(x1.shape[0], v_dim, key_len, query_len)
        # Unpermute the outputs of the dot product attention and the learned positional embedding to return to batched time-steps
        return x1, attention_weights, attention_context
 

class Model(torch.nn.Module):
    def __init__(self, qk_dim, v_dim, dpr=1.0):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim_q=qk_dim, dim_k=qk_dim, dim_v=qk_dim, num_heads=1)
        # Use a learned positional embedding for the key and query to save memory when the model is used on short sentences
        self.attn_pos = torch.nn.Linear(v_dim, qk_dim * 2, bias=False)
 
    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 3, 1).contiguous().view(x1.shape[0], -1, x1.shape[-1])
        v2 = x2.permute(0, 2, 3, 1).contiguous().view(x2.shape[0], -1, x2.shape[-1])
        key_len, query_len = x1.size(-2), x2.size(-2)
        qk_dim, v_dim = self.attn.dim_q, self.attn.dim_v
        # Embed the positional tokens in a learned manner to save memory
        v1 = self.attn_pos(v1).view(-1, query_len, qk_dim * 2)
        v2 = self.attn_pos(v2).view(-1, key_len, qk_dim * 2)
        scaled_qk = self.attn(v1, v2, v2)[0]
        # Use a learned positional embedding to save memory in the softmax computation of the attention mechanism
        attention_weights = scaled_qk.div(np.power(v1.shape[-1], 0.5)).permute(0, 2, 3, 1)
        # Apply dropout before computing softmax and softmax scaling to prevent overfitting
        attention_weights = torch.nn.functional.dropout(attention_weights, p=dpr)
        attention_weights = scaled_qk / np.power(v1.shape[-1], 0.5).permute(0, 2, 3, 1)
        # Compute softmax over the last dimension and apply dropout before computing dot product between query and key to save memory
        attention_weights = torch.nn.functional.dropout(attention_weights, p=dpr
<br>