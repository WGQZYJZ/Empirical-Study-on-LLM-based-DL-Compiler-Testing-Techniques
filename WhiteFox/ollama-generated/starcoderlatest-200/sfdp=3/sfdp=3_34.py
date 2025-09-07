
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(d_model, d_kv)
 
    def forward(self, query, key, value):
        qk  = self.qk(torch.cat((query, key), dim=-1))
        scaled_qk  = qk.mul(scale_factor)
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 3, d_k, d_v).permute(0, 2, 1, 3) # (batch size, d_k, n_heads, d_v // n_heads)
key = torch.randn(1, 3, d_k, d_v).permute(0, 2, 1, 3) # (batch size, d_k, n_heads, d_v // n_heads)
value = torch.randn(1, 3, d_k, d_v).permute(0, 2, 1, 3) # (batch size, d_k, n_heads, d_v // n_heads)
