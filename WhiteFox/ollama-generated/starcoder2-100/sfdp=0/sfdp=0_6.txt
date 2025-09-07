
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale  = torch.sqrt(torch.tensor([1024]))
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
 
        return output


# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(4, 3208576 , 19) # batchsize x dim x seqlength
key    = query
value  = key
 
__output__  = m(query, key, value)

