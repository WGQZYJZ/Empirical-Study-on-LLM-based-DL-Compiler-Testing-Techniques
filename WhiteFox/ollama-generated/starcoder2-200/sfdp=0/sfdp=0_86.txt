
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        # Apply scaling factor `inv_scale` to the input tensor.
        inv_scale  = torch.sqrt(torch.FloatTensor([x]))
        query = torch.randn(8, 32) * inv_scale 
        key = torch.randn(8, 64) * inv_scale # Apply scaling factor `inv_scale` to the input tensor.
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale 
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        value  = torch.randn(8, 64) * inv_scale 
        output = attention_weights.matmul(value) # Apply scaling factor `inv_scale` to the input tensor.
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(32, 8) + 1000  # Adding 1000 to each element of the input tensor is a common practice when scaling down large numbers that may otherwise cause problems with numerical stability.
__output__  = m(x1)

