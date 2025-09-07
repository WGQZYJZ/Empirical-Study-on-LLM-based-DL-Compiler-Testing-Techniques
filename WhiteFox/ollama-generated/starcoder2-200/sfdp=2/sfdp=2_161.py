
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 / inv_scale_factor
        v3  = v2.softmax(dim=-1)
        v4  = v3.dropout(p=dropout_p)
        v5  = v4.matmul(value)


# Initializing the model
m  = Model()

 # Inputs to the model
query  = torch.randn(8, 207, 64, 16)
key    = torch.randn(8, 207, 64, 16)
value  = torch.randn(8, 207, 395, 16)

 # Initializing the parameters used in the model
inv_scale_factor= .5
dropout_p       = .0
__output__     = m(query, key, value)


