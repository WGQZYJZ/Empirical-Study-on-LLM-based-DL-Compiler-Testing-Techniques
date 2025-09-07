
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, hidden_size=0, attn_dropout=0., scale=1e-6):
        super().__init__()
        self.w_q = torch.nn.Parameter(torch.Tensor(*self._key_dims()))
        self.w_k = torch.nn.Parameter(torch.Tensor(*self._value_dims(), hidden_size))
        self.dropout = torch.nn.Dropout(attn_dropout)
        self.scale = scale
 
    def _key_dims(self):
        return self.w_k.shape[1:]

    def _value_dims(self):
        return self.w_v.shape[:2]
 
    def forward(self, query, key, value, mask=None, attn_mask=None):
        # The shape of `query`, `key` and `value` is (batch_size, dim) * (num_heads, head_dim),
        # where num_heads = batch size // head_dim
        # batch size should be a positive integer.
        batch_size = query.shape[0]
        assert isinstance(batch_size, int), 'The model needs to have batch_size as an input'
        if key.ndim != 2:
            raise ValueError('Expected key to be a two dimensional matrix')
        # (batch_size, num_heads * head_dim)
        # (batch_size, dim)
        query = self._reshape(query, batch_size, -1)
        if key.shape[0] != value.shape[0]:
            raise ValueError('Expected key and value to have same batch size')
        # batch size is 1, so num_heads is 1 as well
        # (batch_size) * (head_dim)
        key = self._reshape(key, batch_size, -1)
        # batch size is 1, so num_heads is 1 as well
        # (batch_size) * (head_dim)
        value = self._reshape(value, batch_size, -1)
        dim = query.shape[2]
        # (batch_size) * (num_heads * head_dim), dim:
        # batch size is 1, so num_heads is 1 as well
        # (head_dim) * (num_heads * head_dim), dim:
        attn = torch.bmm(query, key.permute(0, 2, 1)) / self.scale  # (batch_size, dim)
        # batch size is 1, so num_heads is 1 as well
        # (num_heads * head_dim) * (head_dim), dim:
        # batch size is 1, so num_heads is 1 as well
        attn = self._softmax(attn, dim=0)
        # (batch_size) * (head_dim), dim:
        output = torch.bmm(attn, value)
        # return
        # (batch_size) * (dim)
        output = self._reshape(output, batch_size, dim)
        if mask is not None:
            # shape of `mask` is (batch_size, query_length). It has the value 1 at positions where query is not masked and where key or values have a value. If mask is not given, all values are set to 0 for compatibility with the transformer.nn.MultiHeadAttention layer.
            # if mask is None:
            #     return output.masked_fill(mask[:, None] == 0, -float('inf'))
            mask = self._reshape(mask, batch_size, -1)
            # shape of `attn_mask` is (batch_size, dim). If attn_mask is not given, all values are set to 0 for compatibility with the transformer.nn.MultiHeadAttention layer.
            # if attn_mask is None:
            #     return output.masked_fill(attn_mask[:, None] == 0, -float('inf'))
            attn_mask = self._reshape(attn_mask, batch_size, dim)
            output = mask * output + (1 - mask) * attn_mask
        return output
 
    def _softmax(self, x, dim=None):
        