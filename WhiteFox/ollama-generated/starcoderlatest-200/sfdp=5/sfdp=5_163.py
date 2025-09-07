
class Model(torch.nn.Module):
    def __init__(self, d_model, d_kv=None, num_heads=8,
                 dim_feedforward=2048, dropout=0., attention_dropout=0., activation='relu'):
        super().__init__()
        if d_kv is None:
            d_kv = d_model // num_heads * 2

        self.d_kv = d_kv
 
        self.dim_feedforward = dim_feedforward
        self.norm1 = torch.nn.LayerNorm(d_model)
        self.dropout1 = torch.nn.Dropout(attention_dropout, inplace=False)
        self.dropout2 = torch.nn.Dropout(dropout, inplace=False)

        if activation == 'relu':
            self.activation = torch.nn.ReLU()
        elif activation == 'gelu':
            self.activation = torch.nn.GELU()
        elif activation == 'glu':
            self.activation = torch.nn.GLU()

        assert dim_feedforward % 2 == 0 and dim_feedforward != d_model, (
            f"Invalid `dim_feedforward` ({dim_feedforward}) "
            f"for intermediate size.")

        if activation in ('relu', 'gelu'):
            self.linear1 = torch.nn.Linear(d_model, dim_feedforward)
            self.dropout3 = torch.nn.Dropout(dropout, inplace=False)
        else:
            self.linear1 = torch.nn.Conv2d(
                d_model, dim_feedforward, 1, stride=1, padding=0)

        self.norm2 = torch.nn.LayerNorm(dim_feedforward)
        self.linear2 = torch.nn.Linear(dim_feedforward, d_model)
 
    def forward(self, x):
        # q, k, v = x  # Split the inputs into query, key, and value tensors

        if isinstance(x, tuple):
            _, q, k, v = x
        else:
            q, k, v = self.split_inputs(x)
 
        batch_size, len_q, d_k = q.shape
        assert len_q == len_k, "Input query and key length not matched."

        # Multi-head self-attention. Note that in the Transformer paper authors propose different linear layers for queries and keys.
        dim_kv = self.d_kv // 2  # dimension of the key/value space per head
        heads = q.shape[0] // (batch_size * num_heads)
        scaled_attn_weight = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(dim_kv)

        if self.d_kv > 0:
            # Scale the attention weights to prevent numerical overflows
            scaled_attn_weight += attn_mask.unsqueeze(1).unsqueeze(2).repeat(1, heads, q.shape[2], k.shape[-1])  # Add the attention mask to scaled dot product
        else:
            scaled_attn_weight = scaled_attn_weight + attn_mask.unsqueeze(1).repeat(1, heads, q.shape[2], k.shape[-1])  # Add the attention mask to scaled dot product
 
        softmax_scaled_attn_weight = torch.softmax(scaled_attn_weight, dim=-1)  # Apply softmax
        attn_output = self.dropout1(softmax_scaled_attn_weight) @ v  # Compute the dot product of the query and key
        attn_output = self.norm1(attn_output + q).transpose(1,2) # Add residual

        if activation in ('relu', 'gelu'):
            attn_output = self.linear1(attn_output)
            attn_output = self.dropout3(attn_output)
            attn_output = self.activation(attn_output)
 
        attn_output = torch.matmul(attn_output, v)  # Compute the dot product of the attention output and the value
        if activation in ('relu', 'gelu'):
            attn_output = self.linear2(attn_output)

        return attn_output

    def split_inputs(self, x):
        q, k, v = torch.chunk(x, 3, dim=-1)
        # q, k, v = map(lambda t: t.transpose(0, 1), (q, k, v))
        assert tuple(q.shape[0:-2]) == tuple(k.shape[0:-2]), "Inconsistent batch dimensions."
        return q, k, v


# Initializing the model
m = Model(d_model=512)


# Inputs to the model
x = torch.randn(3, 16, 512)
