
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads, dim_model=None):
        super().__init__()
        self.dim_model = dim_model  # The model dimensionality

        # This function defines the `num_heads` times same query and key tensor pairs.
        self._make_query_key_pairs = lambda x: torch.cat([x] * num_heads, dim=2)

    def forward(self, query, key, value):
        batch_size, seq_length, _  = query.shape
        if self.dim_model is not None:
            assert query.shape[1] == key.shape[0] and query.shape[1] == value.shape[0] and \
                   query.shape[2] == self.dim_model and key.shape[2] == self.dim_model and value.shape[
                    2] == self.dim_model
        # Generate query, key, and key tensor pairs with the shape of (batch_size, seq_length, num_heads * dim_model)
        query = self._make_query_key_pairs(query).view(batch_size, seq_length, -1)
        key   = self._make_query_key_pairs(key).view(batch_size, seq_length, -1)

        # Compute the dot product of the query and the key
        qk = torch.matmul(query, key.transpose(-2, -1))  # shape: (bsz, seqlen, seqlen) x (seqlen, dim_model, num_heads * dim_model)

        # Scale the dot product by the inverse scale factor
        inv_scale_factor = 1 / math.sqrt(self._get_dim())  # shape: (bsz, seqlen, seqlen) x (seqlen, dim_model, num_heads * dim_model)
        scaled_qk = qk.div(inv_scale_factor).softmax(-1)

        # Apply dropout to the softmax output
        # shape: (bsz, seqlen, dim_model) * (seqlen, dim_model, num_heads * dim_model)
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)

        # Compute the dot product of the dropout output and a value tensor
        output  = dropout_qk.matmul(value) # shape: (bsz, seqlen, dim_model), (seqlen, dim_model, num_heads * dim_model) x (dim_model, num_heads * dim_model, seqlen)

        return output

    def _get_dim(self):
        if self.dim_model is not None:
            return self.dim_model
        else:
            raise Exception("Cannot compute the dimension of a `None` input.")
# Initializing the model
ma = MultiHeadAttention()

# Inputs to the model
query = torch.randn(1, 8, 64, 64)  # shape: (bsz, dim_model, seqlen)
key   = torch.randn(1, 8, 64, 64)  # shape: (bsz, dim_model, seqlen)
value = torch.randn(1, 8, 64, 64)  # shape: (bsz, dim_model, seqlen)
