
class Model(torch.nn.Module):
    def __init__(self, dim_q, dim_k, num_heads, num_units):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=num_heads, key_dim=dim_k)

    def forward(self, q1, k1, v1, scale_factor):
        v2  # (batch_size * num_heads, seq_len, head_dim), value is ignored here

        self.attention.__init__(query_dim=dim_q, key_dim=dim_k, out_dim=num_units)
        
        self.scaled_qk = qk.div(scale_factor).softmax(dim=-1)
        self.dropout_qk = torch.nn.functional.dropout(self.scaled_qk, p=dropout_p)
        self.output = dropout_qk.matmul(v2)

        return self.output

    # Add the following method for the class MultiheadAttention
    def forward(self, q1, k1, v1, scale_factor):
        scaled_qk  # (batch_size * num_heads, seq_len, head_dim), shape of query after scaling by a constant
        softmax_qk  # (batch_size * num_heads, seq_len, num_units), shape of the result of applying the softmax to the scaled dot product

        self.attention.__init__(query_dim=q1.shape[-1], key_dim=k1.shape[-2], out_dim=v1.shape[-2])
        self.softmax_qk = torch.nn.functional.dropout(self.scaled_qk, p=dropout_p)

        # This line is important for using the MultiheadAttention class, but you do not need it if your model does not use it
        out  # (batch_size * num_heads, seq_len, num_units), shape of the output after applying attention
        self.output = softmax_qk.matmul(v2)
        
        return self.output


# Initializing the model
m = Model()


# Inputs to the model
q1  # (batch_size, num_query, length_query), shape of the query tensor
k1  # (batch_size, num_key, length_key), shape of the key tensor
v1  # (batch_size, num_value, value_dim) or (batch_size, seq_len, num_value, value_dim), shape of the value tensor
scale_factor  # float


