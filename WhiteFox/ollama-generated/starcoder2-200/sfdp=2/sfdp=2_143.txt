
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_, dropout_p_=0.1, inv_scale_factor=512):
 
        query  = query_.transpose(-2, -1)
        key  = key_.transpose(-2, -1)
        value  = value_.transpose(-2, -1)
        qk  = torch.matmul(query, key)
        scaled_qk  = qk.div(inv_scale_factor)
        softmax_qk  = scaled_qk.softmax(dim=-1)
 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p_)
 
        output  = dropout_qk.matmul(value)
        return output
