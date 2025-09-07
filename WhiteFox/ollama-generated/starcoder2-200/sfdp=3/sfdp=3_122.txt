
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled  = torch.matmul(query, key.transpose(-2, -1)) / scale_factor
        softmaxed  = scaled.softmax(dim=-1)
        droped  = torch.nn.functional.dropout(softmaxed, p=dropout_p) 
        return droped.matmul(value)


# Initializing the model
m  = Model()

 # Inputs to the model
 query  = torch.randn(batchsize, num_heads, length, embeddim /num_heads )
  key  = torch.randn(batchsize, num_heads, length, embeddim/num_heads)
 value  = torch.randn(batchsize, num_heads, length, embeddim/num_heads)

