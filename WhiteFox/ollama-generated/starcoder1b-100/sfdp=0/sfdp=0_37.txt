
class ScaledDotProductAttention(nn.Module):
    def __init__(self, config, qkv):
        super().__init__()

        self.qkv = qkv
        self.scale = config.scaled_dot_product_attention_dropout
        self.key_depth  = config.hidden_size // 8
        self.query_depth = config.hidden_size // 8
 
    def forward(self, hidden, attention_mask):
        assert (attention_mask is not None) ^ ((self.config.use_qkv) ^ (self.config.output_scaling))

        # hidden shape: [batch size, seq len, depth]
        # attention mask shape: [batch size, seq len, seq len]

        batch_size = hidden.shape[0]
        seq_len  = hidden.shape[1]
        input_dim = hidden.shape[2]

        hidden_depth = hidden.shape[3]
        assert (input_dim == self.key_depth) ^ ((self.config.use_qkv) ^ (self.config.output_scaling))

        if not(self.config.use_qkv):
            hidden_depth  //= 2
            hidden_depth  = min(self.key_depth, hidden_depth)
        elif self.config.output_scaling:
            hidden_depth //= 8
 
        qk, v = self.qkv[0], self.qkv[1]

        # hidden_shape is [batch size * seq len, hidden size]
        hidden = hidden[:, :, :hidden_depth].contiguous()

        # Calculate the dot product matrix (QK)
        if self.config.use_qkv:
            batch_size //= 2
            assert (qk.shape[1] == self.key_depth) ^ ((self.config.output_scaling) ^ (self.config.use_qkv))
            qk, v = qk[:, :hidden_depth], v[:, :hidden_depth]
        qk = qk.contiguous()
        batch_size, seq_len, input_dim  //= qk.shape[0], qk.shape[1], qk.shape[2]

        scaled_dot_product = torch.matmul(qk, v) / self.scale
 
        if not self.config.use_qkv:
            # (batch_size * seq_len, key_depth) * (key_depth, hidden_depth) => [batch size, hidden_depth]
            assert (qk.shape[0] == v.shape[0]) ^ ((self.config.output_scaling) ^ (self.config.use_qkv))
            qk = qk.view(-1, self.key_depth).contiguous()
            batch_size, seq_len //= qk.shape[0], qk.shape[1]
            scaled_dot_product = scaled_dot_product.reshape(batch_size * seq_len, -1)

        # (batch_size * seq_len, key_depth) => [batch size, hidden_depth]
        assert (qk.shape[0] == v.shape[0]) ^ ((self.config.output_scaling) ^ (self.config.use_qkv))
        scaled_dot_product = scaled_dot_product.contiguous().view(batch_size * seq_len, -1).softmax(-1)
 
        # Multiply the query tensor by the attention weights
        batch_size, seq_len  //= v.shape[0], v.shape[1]
        qk = qk.contiguous()
        output = torch.matmul(v, scaled_dot_product) * attention_mask

        if not self.config.use_qkv:
            # (batch_size * seq_len, hidden_depth) => [batch size, seq len, hidden_depth]
            assert (hidden.shape[0] == output.shape[0]) ^ ((self.config.output_scaling) ^ (self.config.use_qkv))
            batch_size, seq_len  //= output.shape[0], output.shape[1]
            output = output.reshape(batch_size * seq_len, -1, hidden_depth).contiguous()

        # (batch_size * seq_len, hidden_depth) => [batch size, seq len, hidden_depth]
        assert (hidden.shape[0] == output.shape[0]) ^ ((self.config.output_scaling) ^ (self.config.use_qkv))
        output = output.contiguous().view(batch_size * seq_len, -1, hidden_depth)

        # Sum all the outputs
        assert (hidden.shape[0] == output.shape[0]) ^ ((self.config.output_scaling) ^ (self.config.use_qkv))
        batch_size //= output.shape[0]
        return output


# Initializing the model
m = ScaledDotProductAttention()
