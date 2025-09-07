
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Query input with shape [2560, 768] and key value input with shape [32768000, 768], with 2560 queries each and a batch size of 32.
        query = torch.randn(2560, 768) 
        key_value = torch.randn(32768000, 768).reshape([160000, 4096])
        value = self._scaled_dot_product_attention(query=query, key_value=key_value) # Scale the dot product by the inverse scale factor and softmax is applied.
        return value
    def _scaled_dot_product_attention(self, query: torch.Tensor, key_value: torch.Tensor): 
        qk  = torch.matmul(query, key_value.transpose(-2,-1)) # Compute the dot product of a query and a key.
        scale_factor = math.sqrt(float(key_value.shape[-1]))
        scaled_qk  = qk / float(scale_factor) 
        output = scaled_qk.softmax(dim=-1).matmul(key_value) # Apply softmax to the scaled dot product and compute the dot product of a dropout output (scaled dot product) with value.
        return output

# Initializing the model
m  = Model()
 
# Inputs to the model
input1= torch.randn(2560,768)
__output__  = m(input1)

