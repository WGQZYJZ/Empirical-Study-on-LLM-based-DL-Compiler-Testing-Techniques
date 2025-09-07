
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        key = torch.randn(32, 16)
        value = torch.randn(48, 16)
        scale_factor = torch.rand(32, 16).mul(0.5).add_(0.99)
 
        vq  = torch.nn.functional.layer_norm(query + key) 
        # Normalize the query and key tensors.
        vk  = torch.nn.functional.layer_norm(key + value) 
        # Normalize the key and value tensors.
 
        v1 = vq * scale_factor[:, None] # Scale the dot product by a factor.
        v2 = torch.softmax(v1, dim=-1)
        # Apply softmax to the scaled dot product.
 
        v3  = torch.nn.functional.dropout(v2, p=0.5) 
        # Apply dropout to the softmax output.
        v4 = torch.nn.functional.layer_norm(value) 
        # Normalize the value tensor.
        v5 = v3 @ v4 # Compute the dot product of the dropout output and the value tensor.
 
        return vq, v2


# Initializing the model
m  = Model()
 
# Inputs to the model
query  = torch.randn(16, 32) 
 
# Call the forward method for obtaining the outputs from the model.
output_one, output_two  = m(query)
 
