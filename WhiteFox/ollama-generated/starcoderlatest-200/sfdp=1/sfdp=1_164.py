
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=1):
        super().__init__()

        self.num_heads = num_heads

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        batch_size, _, d_k, _ = query.shape

        # Split the queries, keys and values into heads
        q = self._split_heads(query)
        k = self._split_heads(key)
        v = self._split_heads(value)

        # Perform the dot product between all heads
        kq = torch.einsum('bnmd,bnmd->bmnm', q, k)  # (bs, n_heads, nhid/n_heads, n_hid) * (bs, n_heads, n_hid/n_heads, d_k) -> (bs, n_heads, nhid, d_k)

        # Scale the dot product by inverse scale factor
        scaled_kq = kq.div(inv_scale_factor)  # (bs, n_heads, nhid, d_k) / (bs, 1, 1, d_k) -> (bs, n_heads, nhid, d_k)

        # Apply softmax to the dot product and store it in a new variable
        softmax_kq = scaled_kq.softmax(dim=-1)  # (bs, n_heads, nhid, d_k) * Softmax -> (bs, n_heads, nhid, d_k)

        # Dropout applied to the attention weights prior to computing the final output
        dropout_kq = torch.nn.functional.dropout(softmax_kq, p=dropout_p)  # (bs, n_heads, nhid, d_k) -> (bs, n_heads, nhid, d_k)

        # Compute the dot product of the attention weights and values
        out = torch.einsum('bmnm,bmnm->bnmd', dropout_kq, v)  # (bs, n_heads, nhid, d_v) * (bs, n_heads, nhid, d_k) -> (bs, n_heads, bnid/n_heads, d_v)

        # Combine the heads together back into a single tensor
        output = self._combine_heads(out)  # (bs, n_heads*nhid, d_v)

        return output

    def _split_heads(self, x):
        