
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:

        qk = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        qk += self.mask_value
        
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ value # Compute the dot product of the attention weights and the value

        return output

# Initializing the model
m  = ScaledDotProductAttention()

# Inputs to the model
q  = torch.rand(32, 16) * 50 + 1e-9 # A tensor representing a query vector (in our case, it is randomly initialized with small numbers that are close to zero). It has shape [batch_size, d] where batch_size is the number of sequences in the batch and d is the length of each sequence.
k  = torch.rand(32, 16) * 50 + 1e-9 # A tensor representing a key vector (in our case, it is randomly initialized with small numbers that are close to zero). It has shape [batch_size, d] where batch_size is the number of sequences in the batch and d is the length of each sequence.
v = torch.rand(32, 16) # A tensor representing a value vector (in our case it is randomly initialized with small numbers that are close to zero). It has shape [batch_size, d] where batch_size is the number of sequences in the batch and d is the length of each sequence.
