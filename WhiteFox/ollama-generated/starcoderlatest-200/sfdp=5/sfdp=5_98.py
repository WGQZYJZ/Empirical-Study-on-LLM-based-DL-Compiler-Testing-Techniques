
class TransformerAttention(torch.nn.Module):
    def __init__(self, query_dim, key_dim, output_dim):
        super().__init__()
        self.query = torch.nn.Linear(query_dim, output_dim) # Apply a linear projection of the input query with 64 dimensions to 64
        self.key = torch.nn.Linear(key_dim, output_dim)    # Apply a linear projection of the key with 128 dimensions to 128
        self.value = torch.nn.Linear(key_dim, output_dim)  # Apply a linear projection of the value with 64 dimensions to 128
 
        self.dropout_p = 0.3

    def forward(self, query, key, value, attn_mask):
        qk = torch.matmul(query, self.key.weight.transpose(-2, -1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weights = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = torch.matmul(attn_weights, self.value.weight) # Compute the dot product of the dropout output and the value
 
        return output
 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128 * 4, 64 * 256)    # Apply a linear projection of the query with 128 dimensions to 64
        self.key = torch.nn.Linear(128 * 4, 64 * 256)       # Apply a linear projection of the key with 64 dimensions to 128
        self.value = torch.nn.Linear(128 * 4, 64 * 256)     # Apply a linear projection of the value with 64 dimensions to 64
 
        self.attn = TransformerAttention(query_dim=self.key.out_features, key_dim=self.value.out_features, output_dim=self.attn_output_dim)
 
        self.dropout_p = 0.3
 
    def forward(self, input):
        query = torch.matmul(input, self.query.weight)           # Compute the dot product of the query and key with 64 dimensions to 128
        key = torch.matmul(input, self.key.weight)              # Compute the dot product of the query and key with 64 dimensions to 128
 
        attn_mask = torch.randn(query.shape[:2], device=self._device).bernoulli() < 0.1    # Generate a binary mask (with 1s on entries where an element is zero) with shape [batch_size, seq_len]
        attn_output = self.attn(query=query, key=key, value=input, attn_mask=attn_mask)        # Apply the Transformer attention layer
 
        return attn_output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4 * self.attn_dim, 2048, 2048, device=device)    # Batch of four images with dimensions [batch_size, channels, width, height]
