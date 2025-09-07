
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask):
        qk  = torch.einsum("...sd,...sk->...skd", [query, key]) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors. This operation is performed along dimension s. 
        qk  = qk + attn_mask  # Add the attention mask to the result
        attn_weight  = torch.softmax(qk, dim=-2) # Apply softmax to the scaled dot product result
        output = attn_weight @ value  # Compute a weighted sum of the values using the computed weights 
        return output

# Initializing the model
attn = Attention()
 
query = torch.rand([384])  # The query tensor, which is a vector with shape [384] in this example. It represents a query to be used for attention. In general, it can represent different queries of different sizes.
key = torch.rand([256])  # The key tensor, which is a vector with shape [256] in this example. It also represents the keys that will be queried. In general, these could represent different keys that are queried.
value = torch.rand([768]) # The value tensor, which is a vector of shape [768]. This vector represents the values to be attended. Again, in general, this can be any number of dimensions. 
attn_mask = torch.zeros([384, 256])  # The attention mask that will apply on the scaled dot product output of the model. It is a matrix with shape [384 x 256], where each row corresponds to one of the queries and each column correspond to one of the keys.

# Attention mask
attn_mask = torch.nn.utils.rnn.pad_sequence(list(attn_mask), batch_first=True, padding_value=-1e32)  # Pad the attention masks so that they have a shape [batch size x sequence length]. This operation is required to ensure that these tensors can be fed into the Transformer's attention mechanism correctly.
attn_mask = attn_mask == -1e32  # Create a boolean mask for the values in this matrix. In this example, we use -1e32 to indicate an invalid value, and the rest of the elements should be valid inputs.

 # Inputs to the model
__output__  = att(query, key, value, attn_mask)
 
# Attention mask
attn_mask  = torch.nn.utils.rnn.pad_sequence(list(attn_mask), batch_first=True, padding_value=-1e32)
 
 # Inputs to the model
__output__  = att(query, key, value, attn_mask)