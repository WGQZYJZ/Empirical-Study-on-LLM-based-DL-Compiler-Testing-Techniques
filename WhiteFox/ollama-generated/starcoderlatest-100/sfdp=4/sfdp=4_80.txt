
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads, d_model, dropout=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.attention_dropout = torch.nn.Dropout(p=dropout)
        self.value_dropout = torch.nn.Dropout(p=dropout)
 
        # The input projection layer will be applied to the query, key, and value,
        # followed by linear transformation with the dimension of d_k (default 64),
        # and finally transposed back to d_v dimensions. We can see that
        # d_k * num_heads == d_model for simplicity of computation
        self.query_layer = torch.nn.Linear(d_model, d_model, bias=False)
        self.key_layer = torch.nn.Linear(d_model, d_model, bias=False)
        self.value_layer = torch.nn.Linear(d_model, d_model, bias=False)
 
        # The linear transformation will be applied to each of the heads with their own output
        # which is equal to d_model / num_heads
        self.output_layer = torch.nn.Linear(d_model, d_model, bias=False)
 
    def split_heads(self, x):
        return x.view(-1, x.size(1), self.num_heads,
                       int(x.size(-1) / self.num_heads))
 
    def forward(self, query, key, value, attn_mask=None):
        # [B, Tq, dmodel] -> [B, num_heads, Tq, d_k]
        query = self.query_layer(query)
 
        # [B, Tv, dmodel] -> [B, num_heads, Tv, d_k]
        key = self.key_layer(key)
 
        # [B, Tv, dmodel] -> [B, num_heads, Tv, d_v]
        value = self.value_layer(value)
 
        # Split the multi-head query, key and value into the heads of different size
        qh, kh, vh = self.split_heads(query), self.split_heads(key), self.split_heads(
            value)
        num_att_heads = qh.size(-2)
 
        # Split the dimension with the same length to the num_att_heads dimensions
        qh, kh, vh = map(lambda x: x.transpose(-1, -3), (qh, kh, vh))
 
        if attn_mask is not None:
            assert attn_mask.size()[:2] == (value.size(-2), key.size(-2)), \
                f"The size of the `attn_mask` should be (T, T)"
 
        # Perform a multi-head attention
        # [B, num_heads, Tq, dmodel/num_heads] @
        #   [B, num_heads, d_k, d_v] ->
        #   [B, num_heads, Tq, d_v]
        attn_weights = torch.bmm(qh, kh)
 
        if attn_mask is not None:
            attn_weights += attn_mask
 
            # Clip the weights (e.g., in case of numerical overflow)
            attn_weights = torch.softmax(attn_weights, dim=-1)
        else:
            attn_weights = torch.softmax(attn_weights, dim=-1)
 
        attn_weights = self.attention_dropout(attn_weights)
 
        # [B, num_heads, Tq, d_v] -> [B, num_heads, d_v, Tq]
        attn_out = torch.bmm(attn_weights, vh)
 
        if qh is not None:
            attn_out = (
                # [B, Tq, d_v] @ [B, d_v, dmodel/num_heads] -> [B, Tq, dmodel/num_heads]
                torch.transpose(attn_out, -1, -2)
 
                # Transpose back to the original dimension
                + qh
            )
 
        attn_out = self.output_layer(attn_out)
        attn_out = self.value_dropout(attn_out)
 
        return attn_out
# Initializing the model
m = MultiHeadAttention()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
