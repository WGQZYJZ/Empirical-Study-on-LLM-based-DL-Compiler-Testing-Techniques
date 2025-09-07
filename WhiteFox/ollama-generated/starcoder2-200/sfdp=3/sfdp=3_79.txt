
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value): 
        v1  = torch.matmul(query, key.transpose(-2,-1))
        scale_factor = v1 * -0.8639754
        # print("scale_factor", scale_factor)
        v2 = torch.nn.functional.softmax(scale_factor, dim=-1)
        # print("v2.shape", v2.shape)
        dropout_qk  = torch.nn.functional.dropout(v2, p=0.75, training=True)
        # print("dropout_qk.shape", dropout_qk.shape)
        v3 = dropout_qk.matmul(value)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(1,256,7,7).float()
key = query
value = torch.randn(1, 50, 49).float()
__output__  = m(query, key, value)

