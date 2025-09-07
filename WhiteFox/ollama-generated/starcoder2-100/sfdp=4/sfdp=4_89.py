
import torch  # Importing torch in the model file
import math    # Importing math module in the model file
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        # Compute dot product of query and key, then scale it
        qk = torch.matmul(query, key.transpose(-2,-1)) / math.sqrt(query.size(-1))
 
        if attn_mask is not None:
            # Add attention mask to scaled dot product results 
            qk += attn_mask
 
        attn_weights = torch.softmax(qk, dim=-1)  # Compute the softmax of dot-product output
        output = torch.matmul(attn_weights, value) 
        return output


# Initializing the model
model = Model()
 
# Defining some tensors as inputs to the model (i.e., query and key tensors in this case)
query = torch.randn(256, 64, 3072) # A 3D tensor with shape [256 x 64 x 3072]
key = torch.randn(1024, 64, 3072)   # A 3D tensor with shape [1024 x 64 x 3072]
 
attn_mask = torch.zeros([256, 1024], dtype=torch.int8).to(query.device) 
# Create an attention mask of shape [batch size x num of heads] with zeros

# Computing model output using the inputs defined above and an attention mask (optional in this case):
output = model(query, key, query, attn_mask=attn_mask) # Compute model output
 