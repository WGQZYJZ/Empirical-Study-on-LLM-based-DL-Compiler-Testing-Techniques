
class Model(torch.nn.Module):
    def __init__(self, num_queries, dim_head, num_heads, dim_feedforward=None, attn_dropout=0.0, ff_dropout=0.1):
        super().__init__()

        self.num_query = num_queries
        self.dim_head = dim_head
        self.num_heads = num_heads
        self.dim_feedforward = dim_feedforward if dim_feedforward else int(np.floor(self.dim_head * 4))
        self.scale = torch.Tensor([0., 1.]).to(device)
        self.dropout = torch.nn.Dropout(attn_dropout + ff_dropout)

        self.proj_attn = torch.nn.Linear(num_heads, dim_feedforward)
        self.proj_ffn = torch.nn.Linear(self.dim_feedforward, self.dim_head)
        self.attn_layer_norm1 = TLN(self.dim_head)
        self.attn_layer_norm2 = TLN(self.dim_head)
        self.pos_enc_layer_norm = TLN(self.dim_head)

        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, q, k, v):

        # Query, Key and Value are batch-stacked matrices. We flatten them to 2D vectors (batch x sequence_length x input_size).
        query = q.view(-1, self.num_query, self.dim_head)
        key = k.view(-1, self.num_heads, self.dim_head)
        value = v.view(-1, self.num_heads, self.dim_head)

        # Compute attention weights over query and key, then mask out padding values using the mask variable.
        batch_size = query.shape[0]
        head_num = self.num_heads

        attn_weights = torch.matmul(query, key).div(np.sqrt(self.dim_head))  # Batch x head_num x query_length x key_length
        attn_weights = self.dropout(attn_weights)
        attn_weights = attn_weights.view(batch_size, head_num, -1)

        attn_bias = torch.zeros(attn_weights.shape[:2] + (head_num,), device=device).view(-1, head_num)
        attn_bias = self.dropout(attn_bias)

        # We need to transpose this mask and the input so that:
        # 1. The mask is applied along the last dimension of both the mask and input (i.e., it takes the form of (batch x head_num x seq_len x seq_len)), where (seq_len, seq_len) are the two dimensions required by the attention layer.
        # 2. The dot product with the value matrix is applied along the first dimension of both the mask and input (i.e., it takes the form of (batch x seq_len x head_num x seq_len)), where (seq_len, seq_len) are the two dimensions required by the dot product layer.
        # Transposing the mask and the input to make them compatible is accomplished by using the [T] constructor.
        attn_bias = attn_bias[None, None, :, :].repeat(1, batch_size, 1, 1)  # Batch x head_num x (seq_len, seq_len)

        # Calculate the output after attention-softmax with a residual connection between each of the heads.
        # We do this by using the [B] constructor so that it is broadcasted to all of the heads (i.e., batch_size x seq_len x num_heads).
        attn_out = torch.einsum('...bdi,bhj->...bih', (attn_weights, value), ([0, 1], [2, 3]))

        # Calculate the output of the fully-connected feedforward layers using the residual connections between each of the heads.
        ffn_out = self.proj_ffn(self.dropout(self.proj_attn(attn_out))))

        # Add a bias to each head's projection so that we have the same shape as the output of the softmax function.
        ffn_out += attn_bias[None, :, None, :].repeat(1, batch_size, 1, 1)
        ffn_out = self.dropout(ffn_out)

        # Apply feed-forward with dropout to produce the output matrix from this final layer.
        return self.softmax(self.proj_ffn(ffn_out))


# Initializing the model
m = Model(num_queries=64, dim_head=128, num_heads=8)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
