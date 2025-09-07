
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 / self.scale_factor
        v3  = scaled_qk.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.8)
        v5  = dropout_qk.matmul(value)
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
query = torch.randn(16, 32)
key   = torch.randn(16, 32)
value = torch.randn(16, 48)
__output__  = m(query, key, value)

