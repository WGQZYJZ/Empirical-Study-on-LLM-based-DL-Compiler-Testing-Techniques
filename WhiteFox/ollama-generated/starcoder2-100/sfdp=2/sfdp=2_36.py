
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_) -> Tuple[Tensor]:
        v1  = torch.matmul(query_, key_.transpose(-2, -1)) # compute dot product of the query and the key 
        v2  = v1 / math.sqrt(key_.shape[-1])  # scale by inverse scaling factor 
        v3  = v2.softmax(dim=-1)  
        v4  = torch.nn.functional.dropout(v3, p=0.1)
        v5  = v4.matmul(value_) # compute dot product of dropout output and value
        return (v1, v2), v3, v4


# Initializing the model
m  = Model()

# Inputs to the model 
query_  = torch.randn(8, 64, 512)
key_   = torch.randn(8, 64, 512)
value_= torch.randn(8, 64, 3072)

