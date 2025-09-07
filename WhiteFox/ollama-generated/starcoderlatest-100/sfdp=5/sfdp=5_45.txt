
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(768, 768)
        self.linear_k = torch.nn.Linear(768, 768)
        self.linear_v = torch.nn.Linear(768, 768)
 
    def forward(self, q):
        k = self.linear_q(q).view(-1, 256, 2048) # Flatten the query vector and add the batch dimension to its shape. Reshape it to [batch_size, number_of_query_features, 768]. 
        v = self.linear_v(q).view(-1, 256, 1280)
        k = k.transpose(-3, -2) # Swap the last two dimensions of `k`
        qk = torch.einsum('...ji,...jk->...ij', (k, v)) # Compute the dot product of query and key vectors 
        attn_mask = get_attn_pad_mask(q).unsqueeze(1).repeat([1, 256, 1, 1]) # Create an attention mask for q
        attn_weight = torch.softmax(qk + attn_mask * -1e9, dim=-1) # Compute the softmax of the scaled dot product of query and key, add a padding token to avoid division by zero
        output = torch.einsum('...ij,...jk->...ik', (attn_weight, v)) # Perform matrix multiplication to compute the weighted averages. Reshape the result to [batch_size, number_of_query_features, 768]. This has the same shape as `q`.
        output = output.view(-1, q.size(1), q.size(2) * q.size(3)) # Flatten the result back to its original shape
        return attn_weight, output


# Inputs to the model
attn_mask = get_attn_pad_mask(q).unsqueeze(1).repeat([1, 256, 1, 1]) # Create an attention mask for q
qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
qk = qk + attn_mask # Add the attention mask to the scaled dot product


# Attention module
attn_weight, output = Attention()(qk)

