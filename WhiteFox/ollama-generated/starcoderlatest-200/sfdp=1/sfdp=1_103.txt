
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        query  = q1
        key    = k1
        value  = v1
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)).div(10) 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) 
        output = dropout_qk.matmul(value) 
        return query, key, value


# Inputs to the model
q1  = torch.randn(1, 8, 64, 64)
k1  = torch.randn(2, 8, 64, 64)
v1  = torch.randn(3, 8, 64, 64)

