
class Model(torch.nn.Module):
    def __init__(self, n_head, d_model=256, dropout_p=0.3):
        super().__init__()
 
        self.n_head = n_head
        self.d_k    = int(d_model / n_head)
        self.q      = torch.nn.Linear(d_model, n_head * d_k, bias=False) # q is the query in the attention mechanism
        self.kv     = torch.nn.Linear(d_model, n_head * 2 * d_k, bias=False) # kv is a pair of values in the attention mechanism
 
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def split_and_concat(self, h):
        b, l, _  = h.shape  # b: batch size, l: sequence length
        h1      = h.view(b, l, self.n_head, -1)  # [b, l, n_head, d_k]
        h2      = torch.cat((h1[:, :, :, :self.d_k], h1[:, :, :, self.d_k:]), dim=-1)  # [b, l, n_head, d_model]
        return h2
 
    def forward(self, q, k, v):
        # (q: [b, l, d_model])
        # (k: [b, m, d_model])
        # (v: [b, m, d_model])
        b      = q.shape[0]
        d_k    = self.d_k
        n_head = self.n_head
 
        query     = self.q(q)  # [b, l, n_head * d_k]
        key       = self.kv(k).reshape(b, -1, 2, n_head, d_k).permute([0, 2, 3, 4, 1]) # [b, n_head, l, m, d_k] -> [b, n_head, m, l, d_k]
        value     = self.kv(v).reshape(b, -1, 2, n_head, d_k).permute([0, 2, 3, 4, 1]) # [b, n_head, m, l, d_k] -> [b, n_head, m, l, d_k]
 
        scaled_qk     = query.matmul(key.transpose(-2, -1)) / math.sqrt(d_k)  # [b, n_head, m, l]
        attention      = self.dropout(scaled_qk.softmax(dim=-1))  # [b, n_head, m, l]
        output     = torch.matmul(attention, value).transpose(2,3).contiguous().view(b, -1, d_k)  # [b, l, d_model]
 
        return self.split_and_concat(output)


# Inputs to the model
q1 = torch.randn(1, 4, 256)
k1 = torch.randn(1, 2, 256)
v1 = torch.randn(1, 3, 256)
