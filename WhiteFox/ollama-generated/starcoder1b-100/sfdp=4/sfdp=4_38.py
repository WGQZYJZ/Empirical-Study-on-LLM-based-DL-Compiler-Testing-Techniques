
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(8, 8)
        self.key    = torch.nn.Linear(8, 4)
        self.value  = torch.nn.Linear(16, 8)
        self.linear = torch.nn.Linear(8, 8)
 
    def forward(self, q, k, v):
        # Compute the dot product of query and key
        d_k = self.query(k).view(-1, 4, 1)  # Convert [batch, seq_len] to [batch x seq_len x 4]
        dots = torch.einsum('bhj,bhk->bhi', q, d_k)  # Perform dot product between query and key. The result is [batch, seq_len, 4].
        # Scale the dot product by sqrt(d_k), which is what you want to do with this output later on.
        dots = dots / math.sqrt(d_k.size(-1))
        # Add the attention mask for numerical stability. The result is [batch, seq_len, 4].
        attn_mask = torch.eye(self.value.weight.shape[-2], device=v.device)
        attn_mask.fill_(0.5)  # Set all elements to be equal to zero.
        dots += attn_mask  # Add the mask to the result.
        # Compute a weighted sum of the value tensor with the results from the dot product calculation.
        weighted_value = torch.einsum('bhj,bhi->bhi', dots, v)  # Perform weighted sum between dot product and value.
        # Use softmax to get the attention weights. The result is [batch, seq_len, 4].
        attn_weights = torch.softmax(weighted_value, dim=-1)  # Apply softmax on the weighted value, which is a normalized vector.
        # Use the attention weights in the final layer to compute a context vector.
        output = torch.einsum('bhj,bhi->bhi', attn_weights, self.linear(v))  # Perform dot product between attention weights and value. The result is [batch, seq_len, 4].
        # Return the output from this layer.
        return output


# Initializing the model
m = Model()


