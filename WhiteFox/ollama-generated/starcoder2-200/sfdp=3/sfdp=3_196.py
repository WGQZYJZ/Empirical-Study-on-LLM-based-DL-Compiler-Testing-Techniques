
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, scale3):
        v0 = torch.matmul(query1, key2.transpose(-2, -1)) 
        v1  = v0 * scale3 
        v2 = v1.softmax(dim=-1) 
        v4  = torch.nn.functional.dropout(v2, p=0.5)
        v5  = self._helper_function(v4) 
        return v5 
 
    def _helper_function(self, input):
         return input * -7 + 6


# Initializing the model
m = Model()
 
# Inputs to the model
query1 = torch.randn(2, 3, 8)
key2 = torch.randn(2, 5, 3, 4)  # Note that the input size of key tensor is [batch_size, num_heads, seq_length, head_dim]
scale3 = torch.tensor([7])
 
# Initializing the parameters used in the model
m1  = m._helper_function(query1).shape #torch.Size([2, 8])
m2  = m(key2, scale3)  # The size of m is [batchsize, numheads, querylength, headdim] which is not equal to [2,5,4,3]
 
