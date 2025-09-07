
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, inv_scale):
        scaled_dot = torch.matmul(query, key.transpose(-2,-1)) / inv_scale 
        attention  =  scaled_dot.softmax(dim=-1)
        output     = attention.matmul(value) # <------ Line 9
        return output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(32, 64)
key    = torch.randn(32, 512)
value  = torch.randn(32, 768)
inv_scale  = torch.rand(32).sqrt() # <------ Line 9 of the model

# Model output: You can check whether the output is correct by computing attention weights and then manually performing the dot product to verify the results are identical. However you do not have to compute the attention weights directly, since they will be used when doing gradient backpropagation anyways (since the scaling is done with a sqrt).
__output__  = m(query, key, value, inv_scale)

