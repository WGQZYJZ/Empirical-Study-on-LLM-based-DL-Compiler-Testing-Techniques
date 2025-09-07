
class Model(torch.nn.Module):
    def __init__(self, n_head=128):
        super().__init__()
        self.n_head = n_head

        self.query  = torch.nn.Linear(768, 3 * n_head) 
        self.key    = torch.nn.Linear(768, 3 * n_head)
        self.value  = torch.nn.Linear(768, 3 * n_head)
 
    def forward(self, x1):
        # Get the query, key and value
        qk = self._attn(x1, x1, x1)
 
        # Scale the dot product by the inverse scale factor
        scaled_qk = qk.div(inv_scale_factor)
 
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)
 
        # Dropout of the softmax output
        dropout_qk = torch.nn.functional.dropout(
            softmax_qk, p=self._get_drop_prob())
 
        # Compute the dot product of the dropout output and the value
        output  = dropout_qk.matmul(self._v(x1))
        return output
 
    def _attn(self, q, k, v):
        batch_size = q.shape[0]
        q_proj = self.query(q).view(batch_size, -1, 3 * self.n_head) 
        k_proj = self.key(k).view(batch_size, -1, 3 * self.n_head) 
        v_proj = self.value(v).view(batch_size, -1, 3 * self.n_head) 

        # Compute the dot product of the query and key
        qk = torch.einsum('b h i d, b h j d -> b h i j', q_proj, k_proj)

        return qk
 
    def _v(self, x):
        batch_size = x.shape[0]
        proj = self.value(x).view(batch_size, -1, 3 * self.n_head) 
        # Compute the dot product of a value with query and key
        value = torch.einsum('b h i j, b h i d -> b h j d', proj, x)

        return value
 
    def _get_drop_prob(self):
        return float(dropout_p)
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(128, 768) # batch size is 128 and embedding dimension is 768


