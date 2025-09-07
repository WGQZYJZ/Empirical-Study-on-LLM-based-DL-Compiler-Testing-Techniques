
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=None):
        super().__init__()
        self.inv_scale = 1 / (2 ** inv_scale)
 
    def forward(self, query: TensorType, key: TensorType, value: TensorType, masking_value=-inf):
        # Compute the scaled dot product
        # [batch_size x num_heads x sequence_length x sequence_length]
        scaled_dot = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
 
        # Create the mask if it's not provided (masking_value == -inf by default)
        batch_size, _, seq_len, _ = scaled_dot.shape
        if masking_value is None:
            masking_value = -inf  # By default we use -infinity as a masking value
 
            # Create the triangular mask with appropriate dimensions (batch size x num heads) 
            diagonal_mask = torch.tril(torch.ones((seq_len, seq_len)), diagonal=0).to(scaled_dot.device)
 
            masking_value = scaled_dot.new_full(scaled_dot.shape, 
                                               masking_value).masked_fill_(diagonal_mask != 1, 
                                                       masking_value)
 
        # Compute the attention weights based on the scaled dot product
        # [batch_size x num_heads x sequence_length x 1]
        attention_weights = scaled_dot.softmax(dim=-1)
 
        # [batch_size x num_heads x 1 x sequence_length]
        masking_weight = (masking_value - 1).tanh()
        attention_weights = torch.masked_fill_(attention_weights, masking_weight < 0.5, 
                                              -inf)
 
        # Compute the weighted sum of the value tensor based on the attention weights
        output = attention_weights * value + (1-attention_weights)*masking_value
 
# Initializing the model and performing forward pass on an input.
        m = ScaledDotProductAttention(inv_scale=4)
 
        batch_size, num_heads, sequence_length, _  = query.shape
        key = key.repeat((num_heads, 1, 1)) # [batch_size x num_heads x sequence_length x sequence_length] 
        value = value.repeat(num_heads) # [batch_size x num_heads x sequence_length x value_size]
 
       __output__  = m(query, key, value)

