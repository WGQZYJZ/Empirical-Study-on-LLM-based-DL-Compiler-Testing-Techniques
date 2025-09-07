
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 / math.sqrt(key.size()[-1]) # Applying scaling
        v3  = v2.softmax(dim=-1)   # Applying softmax
        v4  = dropout(v3, p=0.5, training=training) # Applying dropout
        v5  = v4 * value 
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model 
 query_tensor  = torch.randn([128, 96])
 key_tensor   = torch.randn(query_tensor.size())
 value_tensor  = torch.randn(query_tensor.size())
  __output__  = m(query_tensor, key_tensor, value_tensor)

