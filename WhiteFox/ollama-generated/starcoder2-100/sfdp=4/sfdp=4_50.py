

class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(10, 8)
 
    def forward(self, query, key, value):
        attn = self.attn(query, key, value)[0] + query
        return attn

# Initializing the model
m  = Attention()
 
# Input tensors to the model
input_query  = torch.randn(1024, 384) # A random tensor of shape (batch size, embedding dimensions) for the query vector in the attention mechanism.
input_key  = torch.randn(567, 384) # A random tensor of shape (sequence length, embedding dimension). This is the key used to compute the dot product. The sequence length is a random number between 1 and 200.
input_value  = torch.randn(567, 10, 384) # A random tensor of shape (sequence length, sequence_length', embedding dimension). This is the value used to compute a weighted sum of the dot product of the attention weights and the value vector.
attn_mask  = torch.ones([len(input_key), len(input_value)]) - torch.eye(10) # A mask that is used to prevent attention to certain positions in the sequence length dimension
 
# Running the model on input tensors
output, attn_weights  = m(input_query, input_key, input_value)