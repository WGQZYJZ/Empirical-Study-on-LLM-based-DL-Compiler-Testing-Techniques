

class SelfAttentionLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(768, 3072)
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor, attn_mask=None):
        queryk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, and scale it
 
        if (attn_mask is not None):
            queryk = queryk + attn_mask # Add the attention mask to the scaled dot product
 
        queryk = self.softmax(queryk)  # Apply softmax to the result
        output = torch.einsum('ijk -> jki', queryk) @ value  # Compute the dot product of the attention weights and the value tensor

        return output

attn_mask = torch.full((16, 48), float("-inf"), device="cuda:0")
for i in range(attn_mask.size(-2)):
    attn_mask[:,i] += 2*torch.arange(0, int(attn_mask.size(-2)/3), dtype=torch.int64).repeat((16,)) # Fill the attention mask with a linear sequence that increases by three for every row.
attn = SelfAttentionLayer().to('cuda:0')


output = attn(query.to('cuda:0'), key.to('cuda:0'), value.to('cuda:0'), attn_mask=attn_mask.to('cuda:0'))

m  = m() # Initialize the model
x1  = torch.randn(2,3) # Initialize an input tensor to feed into the model

