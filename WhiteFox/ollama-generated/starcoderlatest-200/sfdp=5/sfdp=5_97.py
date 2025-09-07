
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, n_head: int, d_k: int, d_v: int, dropout_p: float = 0.1):
        super().__init__()
        self.d_k = d_k
        self.n_head = n_head
        self.w_qs = torch.nn.Linear(n_head * d_k, n_head * d_v)
        self.w_ks = torch.nn.Linear(n_head * d_k, n_head * d_v)
        self.w_vs = torch.nn.Linear(n_head * d_v, n_head * d_v)
        self.dropout = torch.nn.Dropout2d(p=dropout_p)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor):
        batch_size = query.shape[0]
        q = self.w_qs(query).view(batch_size, -1, self.n_head, self.d_k) # View as (bsz, seq_len, n_head, d_k)
        k = self.w_ks(key).view(batch_size, -1, self.n_head, self.d_k)
        v = self.w_vs(value).view(batch_size, -1, self.n_head, self.d_v) # View as (bsz, seq_len, n_head, d_v)
 
        q = self.dropout(q)
        k = self.dropout(k)
        v = self.dropout(v)
 
        output = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k) # Compute the scaled dot product of the query and key
        attn_mask  = mask_attn(query, None).unsqueeze(0) # Add a tensor with the same shape as the query with values 0 or 1 to indicate whether the corresponding sequence in the batch should be padded or not.
 
        output = output + attn_mask  # Add the attention mask
        output = torch.softmax(output, dim=-1) # Apply softmax to the result
        output = self.dropout(output) # Apply dropout to the softmax output
        return torch.matmul(output, v) # Compute the dot product of the softmax output and the value
class Model(torch.nn.Module):
    def __init__(self, n_head: int = 16, d_k: int = 56, d_v: int = 80, dropout_p: float = 0.1):
        super().__init__()
        self.attn = MultiHeadSelfAttention(n_head=n_head, d_k=d_k, d_v=d_v, dropout_p=dropout_p)
 
    def forward(self, x1, x2):
        v1 = self.attn(x1, x2)
        return v1
# Initializing the model
m = Model()

