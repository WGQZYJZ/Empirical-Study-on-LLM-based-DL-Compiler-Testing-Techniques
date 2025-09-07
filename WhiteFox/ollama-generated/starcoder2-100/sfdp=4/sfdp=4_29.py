
class MultiHeadAttentionModel(torch.nn.Module):
    def __init__(self, input_dim=768, num_heads=12):
        super().__init__()
        self.input_dim = 768 # Use the default value of 768 as the input dimension
        self.num_heads = 12 # Use the default value of 12 for the number of heads

        # Create the Q, K, V projections based on the input dimensions and the number of heads
        self.q_proj = torch.nn.Linear(input_dim, num_heads * (self.input_dim // self.num_heads)) 
        self.k_proj = torch.nn.Linear(input_dim, num_heads * (self.input_dim // self.num_heads))
        self.v_proj = torch.nn.Linear(input_dim, num_heads * (self.input_dim // self.num_heads))

        # Create the scaling factor to apply in the dot product of the query and key tensors
        self.scaling_factor = input_dim / num_heads 

        # Set the dropout layer using the specified probability 
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, query):

        # Get the batch size for the input
        batch_size = len(query)
        query_proj = self.q_proj(query).reshape(batch_size, -1, self.num_heads, (self.input_dim // self.num_heads))
        key_proj  = self.k_proj(query).reshape(batch_size, -1, self.num_head, (self.input_dim // self.num_heads))

        # Compute the dot product of the query and key tensors, and apply dropout 
        scaled_qk = torch.einsum("bsq, bsk->bsh", query_proj, key_proj) / math.sqrt(self.scaling_factor)
        attn_mask  = torch.ones((batch_size, -1), device=scaled_qk.device) 
        attn_mask[torch.tril(attn_mask)] = float("-inf") 

        scaled_qk = self.dropout(scaled_qk + attn_mask) 

        # Apply the softmax function to compute the attention weights
        attn_weights = torch.softmax(scaled_qk, dim=-1) 

        value_proj  = self.v_proj(query).reshape(-1, -1, num_heads, (self.input_dim // self.num_head))

        # Compute the dot product of the attention weights and the value tensor
        output = torch.einsum("bshq->bsqn", attn_weights @ value_proj) 
        return output


# Initializing the model<|end_of_model|>
m  = MultiHeadAttentionModel()

# Inputs to the model<|end_of_inputs|>
x1  = torch.randn(32, 768)
__output__  = m(x1)

