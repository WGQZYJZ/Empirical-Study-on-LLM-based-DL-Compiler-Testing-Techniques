
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, query_key_dim_mul = 1):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / (query_key_dim_mul ** 0.5)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk @ value
        return output
# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(2, 8, 16, 32)
key = torch.randn(4, 8, 32, 64)

 