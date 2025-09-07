
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(32, 64)
        self.key   = torch.nn.Linear(32, 64)
        self.value = torch.nn.Linear(32, 100)
        self.dropout_p = 0.5
 
    def forward(self):
       qk = torch.matmul(query, key.transpose(-2, -1)) 
       scaled_qk = qk / math.sqrt(self.key.weight.shape[0]) # div the dot product by sqrt of the number of keys in the query
       softmax_qk  = scaled_qk.softmax(dim=-1) # apply softmax to the scaled dot product
       dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) 
       output  = dropout_qk.matmul(value) 
 
       return output

# Initializing the model
m  = Model()

 # Inputs to the model
query1  = torch.randn(32, 64) 
 key1   = torch.randn(32, 64)
 value1 = torch.randn(32, 100)
 
__output__  = m()