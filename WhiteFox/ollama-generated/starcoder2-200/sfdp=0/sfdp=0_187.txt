
class Model(torch.nn.Module):
    def __init__(self, dim_k=None, inv_scale = None):
        super().__init__()
 
        self.dim_k  = torch.nn.Parameter(
            torch.ones(1) * (inv_scale / math.sqrt(float(dim_k))))
 
    def forward(self, query, key, value):
        
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.dim_k
        attention_weights  = scaled_dot_product.softmax(dim=-1)
 
        output = attention_weights.matmul(value)
        return output


# Initializing the model
model = Model()

 # Inputs to the model
query = torch.randn(2,32000/8 ,512).to(torch.float64) 
key   = query
value = key
 
__output__  = model(query=query, key=key, value=value)

