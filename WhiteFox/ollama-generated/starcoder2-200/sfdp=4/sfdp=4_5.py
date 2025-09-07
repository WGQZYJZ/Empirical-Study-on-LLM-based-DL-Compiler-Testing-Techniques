
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask):
        qk  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors with scaling
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ value # Compute a weighted sum of the value tensor using the attention weights
 
        return output

# Initializing the model
model = ScaledDotProductAttention()
 
# Attention mask for model inputs. This mask prevents attention within specific positions in the sequence, such as paddings.
attn_mask  = torch.full((1, 30), -float('inf'), device=device) # Initialize the attention mask with -infinity values
 
# Inputs to the model
query  = torch.randn(16, 256).to(device)
key    = torch.randn(16, 256).to(device)
value  = torch.randn(16, 30, 480).to(device)


# Initializing the model with initial inputs and the mask on the input values
model_inputs   = {'query': query, 'key': key, 'value': value}
attn_mask      = torch.full((256), -float('inf'), device=device) # Initialize the attention mask with -infinity values
 
# Generate a new model
gen_model  = Model(model, model_inputs)

