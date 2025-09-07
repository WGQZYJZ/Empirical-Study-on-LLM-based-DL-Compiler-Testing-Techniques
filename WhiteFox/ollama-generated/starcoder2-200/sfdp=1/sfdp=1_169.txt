
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        inv_scale = torch.Tensor([0.75]).to(query) # The scale factor to be used for the dot product
        inv_scale_factor  = query ** -2 / (inv_scale ** 2 + 1e-9).sqrt()
        
        k1  = query * key.transpose(-2, -1) 
        k2  = torch.nn.functional.softmax(k1/inv_scale_factor, dim=-1)
        k3  = torch.nn.functional.dropout(k2, p=0.75, training=self.training)
        v4  = torch.matmul(k3, value)
        return v4

m  = Model() # Initializing the model

# Input tensors to the model
q1  = torch.randn(64, 8, 8) # The query tensor of shape (batch size, height, width), where batch size is a positive integer.
k1  = torch.randn(64, 8, 32).div(0.75)# The key tensor of shape (batch size, height, width) where batch size is the same as in the query tensor, and scale factor `inv_scale` is `0.75`.
v1  = torch.randn(64, 8, 32).div(0.75)# The value tensor of shape (batch size, height, width) where batch size is the same as in the query tensor, and scale factor `inv_scale` is `0.75`.

# Inputs to the model
