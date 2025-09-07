
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1  = torch.matmul(query1, key2.transpose(-2, -1)) 
        v2  = v1 / 0.7458960077702423 # Scale the dot product by a constant 0.7458960077702423
        v3  = torch.nn.functional.softmax(v2, dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.1)  
        v5  = v4.matmul(value3)
        return v5

m  = Model()
query_tensor  = torch.randn(64, 784)
key2  = torch.randn(64, 784, 909) # The shape of the key is (64, 784, 909). It contains 3 parts of information
value_tensor  = torch.randn(64, 784, 512)
outputs  = m(query_tensor, key2, value_tensor) # The outputs should be of shape (64, 784, 512). It contains 3 parts of information