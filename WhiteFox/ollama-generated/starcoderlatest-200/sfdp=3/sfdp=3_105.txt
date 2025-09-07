
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(dim1=8, dim2=3)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, 8, 64, 64) # (N, E/M, Lq, Dk)
key    = torch.randn(1, 8, 64, 64) # (N, E/M, Lk, Dk)
value  = torch.randn(1, 8, 64, 64) # (N, E/M, Lv, Dv)
