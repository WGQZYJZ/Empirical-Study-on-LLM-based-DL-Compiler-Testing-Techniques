
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.2):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v3  = v1 / math.sqrt(key[0].numel()) # Scale the dot product by a factor
        v4  = v3 * query 
        v5  = value + v4
        return v5
 
# Initializing the model
m = Model()

 # Inputs to the model
query, key, value = torch.randn(1024, 8), torch.randn(1024, 64, 64), torch.randn(1024, 3)
__output__  = m(query, key, value)

