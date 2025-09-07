
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk / 2.0
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(key)
        return output
 

# Inputs to the model
query = torch.randn(2, 3, 64, 64)
key   = torch.randn(2, 3, 64, 64)
