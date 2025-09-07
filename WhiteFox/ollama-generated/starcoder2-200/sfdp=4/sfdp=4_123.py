
class DotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(64, 32)
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor, attn_mask=None) -> Tuple[Tensor]:
        qk = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors 
        if attn_mask is not None:
            attn_mask = attn_mask  # Apply the attention mask to the scaled dot product
        attn_weights = torch.softmax(qk, dim=-1)
        output = attn_weights @ value # Compute a weighted sum of the values tensor using the attention weights
        return output

# Initializing the model
m = DotProductAttention()
 
# Inputs to the model 
query = torch.randn(8,64,32)  # Initialize an input query tensor with shape (batch_size x hidden_dim x key_seq_length), where batch size is 8, and hidden dim is 64, and key sequence length is 32 
key = torch.randn(10,5,32,64) # Initialize an input key tensor with shape (batch_size x query_seq_length x key_sequence_length x hidden_dim), where batch size is 8, the query sequence length is 32, and the key sequence length is 32. 
value = torch.randn(10,5,64) # Initialize an input value tensor with shape (batch_size x sequence_length x hidden_dim). Batch size is 8, key sequence length is 32, and hidden dim is 32 


# Initializing the model