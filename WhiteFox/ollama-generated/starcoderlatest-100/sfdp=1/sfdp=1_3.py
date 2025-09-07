
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(query_dim, key_dim)
        self.v  = torch.nn.Linear(value_dim, query_dim)
 
    def forward(self, q1, k1, v1):
        # Get attention scores for all the keys in the current head
        # qk: (bs, nh, head_num, len_query, len_key) x (bs, head_num, len_key, key_dim) -> (bs, nh, head_num, len_query, key_dim)
        v1 = self.v(v1)  # (bs, nh, query_dim) x (bs, key_dim, value_dim) -> (bs, nh, query_dim)
        qk = self.qk(q1).view(-1, heads, k1.shape[-2], -1).transpose(-2, -1).matmul(k1)  # (bs, head_num, len_query, key_dim) x (bs, key_dim, len_key, value_dim) -> (bs, nh, query_dim)
        scaled_qk = qk.div(inv_scale_factor)  # (bs, nh, query_dim) -> (bs, nh, query_dim)
        softmax_qk = scaled_qk.softmax(-1)  # (bs, nh, len_query, key_dim)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # (bs, nh, len_query, key_dim) -> (bs, nh, len_query, key_dim)
        # Compute the attention output of the current head: a tensor whose size is equal to `(bs, nh, query_dim)`, with each column corresponding to one feature map of the input data
        attention_output = dropout_qk.matmul(v1)  # (bs, nh, len_query, value_dim) x (bs, nh, value_dim, key_dim) -> (bs, nh, query_dim)
        return attention_output


# Initializing the model
m = Model()
# Inputs to the model: a tensor with shape `(bs, query_num, channel, height, width)` where `query_num` means number of queries and `channel`, `height`, `width` represents the dimensions of the input data
attention_output  = m(q1, k1, v1)

