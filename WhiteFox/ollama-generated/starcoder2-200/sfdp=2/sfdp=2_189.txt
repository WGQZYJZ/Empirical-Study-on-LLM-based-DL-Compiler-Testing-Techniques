
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_, dropout_p_=0., scale=1e-4):
        qk  = torch.matmul(query_, key_.transpose(-2, -1))
        scaled_qk  = qk / scale
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p_)
        output  = dropout_qk.matmul(value_)

        return output


# Initializing the model
m  = Model()
 
# Query and key inputs for attention mechanism
query1  = torch.randn(32, 64)
key1   = torch.randn(32, 64)
value1  = torch.randn(32, 80, 512)
 
__output__  = m(query1, key1, value1)

