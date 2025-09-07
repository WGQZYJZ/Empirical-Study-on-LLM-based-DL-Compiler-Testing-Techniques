
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 / 3072
        v3 = v2.softmax(dim=-1)
        v4 = dropout(v3, p=0.5, training=self.training)
        return v4 @ value


# Initializing the model
m  = Model()

 # Inputs to the model
query_t  = torch.randn(64, 8*257, 1)
key_t   = torch.randn(309, query_t.size(-2), 1) / 3072
value_t = torch.nn.functional.linear(key_t, weight=torch.randn(query_t.size(-2)))
 
 __output__  = m(query_t, key_t, value_t)
 