
class AttnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 8) # Create a fully-connected layer with input size of 3 and output size of 8

    def forward(self, query, key, value, attn_mask=None):
        v1  = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) 
        if attn_mask != None:
            v1 += attn_mask # Add the attention mask to the scaled dot product
        v2  = torch.softmax(v1, dim=-1) # Apply softmax to the result
        output = v2 @ value # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m  = AttnModel()

 # Inputs to the model
query = torch.randn(32,80,512)
key   = torch.randn(32,769,512)
value = torch.randn(32,769,1)
attn_mask  = torch.zeros(size=(32,769)) # Zero-out the attention weights to prevent the model from attending to irrelevant positions in the sequence

 ## In this step we will provide a batch of sequences and an attention mask.

query  = query.view(-1,80,512) # Reshape the sequences into a single sequence
key    = key.view(-1,769,512)  # Reshape the sequences into a single sequence
value  = value.view(-1,769,1)  # Reshape the sequences into a single sequence
attn_mask  = attn_mask.repeat(32,1) # Repeat the attention mask for every sequence in the batch
 
__output__  = m(query, key, value, attn_mask=attn_mask) 

