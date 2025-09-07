
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1):
        super().__init__()
        self._scale = 64 ** (-dim // 2)
 
    def forward(self, query, key, value, dropout=0., p=None):
        # Compute dot product of the query and key tensors.
        scaled_qk  = torch.nn.functional.scaled_dot_product(query, key, scale=self._scale)
        softmax_qk  = scaled_qk.softmax(-1)
        if dropout > 0.:
            if p is not None:
                dropout_qk  = dropout(torch.nn.functional.dropout(softmax_qk, p=p), p=0.)
            else:
                dropout_qk  = dropout(softmax_qk,)
        # Compute the dot product of the dropout output and the value tensor.
        return dropout_qk @ value
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self._query  = torch.randn(3, 8)
        self._key   = torch.randn(4, 1024, 768)
        self._value = torch.randn(5, 96, 1024)
 
        self.scaled_dot_product_attention  = ScaledDotProductAttention(-3)
 
    def forward(self):
        # Apply Scaled Dot Product Attention Mechanism.
        v7 = self.scaled_dot_product_attention(
            query=self._query, key=self._key, value=self._value)
