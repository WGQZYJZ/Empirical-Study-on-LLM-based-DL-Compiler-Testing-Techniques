
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, mask=None):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(self.d_k)
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        if mask is not None:
            softmax_qk *= mask
        
        attention = torch.matmul(softmax_qk, v)

        output  = self.out_layer(attention).transpose(-2, -1) * math.sqrt(self.d_k) + q  # Output = Concatenate(Query, Attention) * sqrt(d_k), then Scale by d_k and add Query
        return output


# Inputs to the model
q = torch.randn(batch_size, query_len, self.d_model)
k = torch.randn(batch_size, key_len, self.d_model)
v = torch.randn(batch_size, key_len, self.d_model)
mask = None if (query_len < max_len) else (torch.rand((batch_size, query_len)) > mask_p).unsqueeze(-2).expand(-1, -1, -1, self.d_model).to(q.dtype)
