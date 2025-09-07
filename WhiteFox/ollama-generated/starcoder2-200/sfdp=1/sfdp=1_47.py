
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        v2  = torch.matmul(q1, k1.transpose(-2, -1))
        v3  = v2.div(inv_scale_factor)
        v4  = v3.softmax(dim=-1) 
        v5  = torch.nn.functional.dropout(v4, p=dropout_p) 
        return v5


# Initializing the model
m  = Model()
 
 # Inputs to the model 
 q1  = torch.randn(batchsize, num_heads, query_length, embedding_dim//num_heads)
  k1 = torch.randn(batchsize, num_heads, key_length, embedding_dim//num_heads)
 v1  = torch.randn(batchsize, num_heads, value_length, embedding_dim//num_heads)
 
 # Initializing the parameters 
 inv_scale_factor = 4
 dropout_p = 0.25

 