
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, mask, key):
        v1 = self.conv(x1)
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
 
        # Set the mask on the masked locations with zeros. 
        # This is done in order to avoid any numerical instabilities due to floating point operations on very large inputs
        attn_mask = torch.zeros_like(value)
        attn_mask[mask] = 1 # Set the mask on the masked locations with ones
        output *= attn_mask # Apply attention mask * value
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mask = x1 > 0
key = torch.randn_like(x1, requires_grad=False) # Set the key for each layer to a random vector of length 50.
