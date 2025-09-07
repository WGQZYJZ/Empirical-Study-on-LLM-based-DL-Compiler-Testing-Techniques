
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, query1, key1, value1):
        v1  = torch.matmul(query1, key1.transpose(-2, -1)) 
        v2  = v1 * scale_factor1 
        v3  = v2 .softmax(dim=-1)  
        v4  = torch.nn.functional.dropout(v3, p=dropout_p1)
        v5  = v4.matmul(value1)
        return v5

# Initializing the model with random values
query1  = torch.randn(batchSize, hiddenDim, querySize) * (2 / torch.sqrt(querySize))
key1    = torch.randn(batchSize, hiddenDim, keySize) * (2 / torch.sqrt(keySize))
value1  = torch.randn(batchSize, hiddenDim, valueSize)

 # Inputs to the model 
 __output__  = m(query1, key1, value1)
 