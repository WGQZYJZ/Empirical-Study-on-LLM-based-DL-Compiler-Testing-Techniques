
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, dropout=0., bias=False, add_bias_kv=False):
        super().__init__()
        self._num_heads = num_heads if isinstance(
            num_heads, int) else len(num_heads)

        self.embed_dim = embed_dim
        head_dim  = embed_dim // num_heads
        #  error: pytorch_test:18:25: ERROR: 'torch.nn' module cannot be imported
        # self.in_proj_weight = nn.Parameter(
        #     torch.empty((embed_dim, embed_dim)))

        #  error: pytorch_test:19:27: ERROR: 'torch.nn' module cannot be imported
        # self.in_proj_bias = nn.Parameter(torch.zeros((embed_dim,)))

        self._qkv_same_head = False

        self.dropout = torch.nn.Dropout(dropout)

    def forward(self, query):  # type: (Tensor) -> Tensor
        tgt_len, bsz, embed_dim = query.size()
        head_dim  = embed_dim // self._num_heads
        assert embed_dim % self._num_heads == 0, \
            'embedding dimension must be divisible by num_heads'

        if isinstance(self._qkv_same_head, bool):
            qkv_bias = True
            qkv_linear_weight = self.in_proj_weight
        else:
            qkv_bias = False
            qkv_linear_weight = self.in_proj_weight

        num_batch  = bsz
        #  error: pytorch_test:103:49: ERROR: 'torch.nn' module cannot be imported
        # batch_time_state = torch.zeros((num_batch, head_dim))

        batch_time_q = torch.einsum("bhkd->bhwk", query)

        k  = batch_time_q.clone()
        v  = batch_time_q.clone()

        #  error: pytorch_test:106:34: ERROR: 'torch.nn' module cannot be imported
        # if self._num_heads != 1 and self._qkv_same_head:
            # k = torch.einsum("bhkd,id->bhwk", batch_time_q, self.in_proj_weight)
            # v = torch.einsum("bhkd,id->bhwk", batch_time_q, self.in_proj_weight)
        # elif not self._qkv_same_head:
            # k = torch.einsum("bhid,ihkd->bhwk", batch_time_q, self.in_proj_weight)
            # v = torch.einsum("bhid,ihkd->bhwk", batch_time_q, self.in_proj_weight)
        #  k = torch.einsum("bhkd,id->bhwk", batch_time_q, self.in_proj_weight)

        #  error: pytorch_test:109:58: ERROR: 'torch.nn' module cannot be imported
        # batch_time_state += torch.einsum('bhwk,bhwk->bh', k, v).detach()

        batch_time_state = batch_time_q * 2
        
        qkv_bias = True if self._num_heads != 1 and self._qkv_same_head else False
        #  error: pytorch_test:130:59: ERROR: 'torch.nn' module cannot be imported
        # k = self.linear_weights(batch_time_state, batch=True).view(num_batch, -1, self._num_heads)

        return batch_time_q


m  = MultiHeadSelfAttention()
__output__  = m(x2)

x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(2058, 1973, 768)

