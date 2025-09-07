

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.scale = 5000
        
        # The weight vector to be multiplied by the query and then passed through a dot product with the key vector, then added to the mask value tensor at each position
        self.linear_weight = torch.nn.Linear(d_model, d_model)

        # In PyTorch, there is no bias term in the Linear layer; however, we still add 1D tensors for these purposes
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor = None, mask=None):
        # We pass each matrix through a linear transformation to reduce the number of parameters in the model.
        q = self.linear_weight(query)
        k = self.linear_weight(key)

        # Compute the dot product of these matrices and normalize it by the square root of the number of features in the query vector (we use the scaling method for this)
        attn_weights  = torch.bmm(q, k.transpose(-2, -1)) / self.scale
        
        if mask is not None:
            # We add a dummy value of one to the mask, so that we do not need to add another value to it
            attn_mask  = torch.ones_like(attn_weights) + mask.float()
            
            # We use an unintuitive notation in PyTorch: for example, the second to last dimension is -2, and then there's nothing to -1 that signifies "first to last"
            attn_weights[attn_mask != 0] = float('-inf')
            
        # Apply softmax along each row (we assume each row contains only positive values because of the scaling method)
        attn_probs = torch.softmax(attn_weights, -1)

        # We multiply by the value tensor to compute a weighted sum of the input value tensors based on these weights
        attn_out  = torch.bmm(attn_probs, value)
        
        return attn_out


# Initializing the model
scaled_dot = ScaledDotProductAttention()
 
# Inputs to the model
q1 = torch.randn(432, 50, 768) # Batch of queries (sequences in the sequence-to-sequence model) with 432 sequences and each sequence contains 50 word embeddings per vector.
k1 = torch.randn(498, 50, 768) # Batch of keys (queries) for these queries. 498 sequences correspond to the queries from the query tensor q1. Each sequence is also 50 words long.
v1 = torch.randn(432, 1, 768)  # Value vector that will be multiplied by each query
attn_mask1 = torch.ones([q1.size(-2), k1.size(-2)]) - float('inf')  # A masking value to prevent attention from the padding sequence positions of both keys and queries. 0 indicates the position to be masked, which will ensure that these values won't get computed in the model.

