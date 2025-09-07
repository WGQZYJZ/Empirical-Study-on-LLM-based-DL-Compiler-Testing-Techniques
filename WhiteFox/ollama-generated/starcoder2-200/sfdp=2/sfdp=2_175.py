
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value): 
        v1  = torch.matmul(query, key.transpose(-2,-1))
        v2  = v1 / math.sqrt(64) #inv_scale_factor
        v3  = v2.softmax(dim=-1)  
        v4  = dropout_p = 0.5
        v5  = torch.nn.functional.dropout(v3, p=v4)
        v6  = torch.matmul(value, v5) 
        return v6


# Initializing the model
m = Model()
 
# Inputs to the model
query1 = torch.randn(2048, 64) # query tensor of size (batch_size x key_dim), it can be randomly generated or imported from an external source
key1 = torch.randn(35, 35) # key tensor of size (num_heads * head_dim x key_dim), it is the same size as the query for the first input. It can also be randomly generated or imported from an external source 
value1 = torch.randn(64, 2048) 
 
query2  = torch.randn(35*35, 64) # query tensor of size (num_heads * head_dim x query_dim), it is the same size as the value for the first input. It can also be randomly generated or imported from an external source
key2 = torch.randn(100, 100) # key and value tensors of size ((num_heads + 1)*head_dim x (query + key dim)), it is a multiple of the size of the query for the second input. It can also be randomly generated or imported from an external source
value2 = torch.randn(35*35, 64) 
 
 
# Calculating the model output with a batch_size of 100, key dimension equal to 128 and query dimension equal to 256
__output_1__  = m(query1,key1,value1) # Model output without dropout in the first input for a batch size of 100 with 35 heads (num_heads=35),  each head of size 128 x 256 key/query. 
__output_2__ = m(query2,key2,value2) # Model output without dropout in the second input for a batch size of 300 with 4 heads (num_heads=4), each head of size 128 x 750 key/query. 

# Calculating the model output with a batch_size equal to 1 and query dimension equal to 64
__output_1__ = m(torch.randn(3, 64)) # Model output without dropout in the first input for a batch size of 3 with key/query dimensions of 64 x 128. 
__output_2__ = m(torch.randn(500, 64), torch.randn(30*30+975, 64)) # Model output without dropout in the second input for a batch size of 500 with key/query dimensions of (num_heads+1) x 256. 