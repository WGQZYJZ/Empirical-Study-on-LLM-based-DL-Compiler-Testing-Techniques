
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.conv2 = torch.nn.Conv2d(16, 32, kernel_size=1)
 
    def forward(self, x1):
        qk = torch.einsum('b n d e -> b d e n', (x1, self.key, self.value)) # Apply the Einstein summation convention to compute the attention scores and attention weights
        attn_weight  = torch.softmax(qk, dim=-1)  # Compute the softmax of the scaled dot product of the query and key (plus an attention mask)
        output = self.attn_combine(x1, x1, x1 * attn_weight)  # Multiply each query by its corresponding attention weights, combine them with the key (and value) to form a multi-head attentive context vector, and then apply the linear layer
        return output
 
    def forward(self, x1):
        qk = torch.einsum('b n d e -> b d e n', (x1, self.key, self.value)) # Apply the Einstein summation convention to compute the attention scores and attention weights
        attn_weight  = torch.softmax(qk, dim=-1)  # Compute the softmax of the scaled dot product of the query and key (plus an attention mask)
        output = self.attn_combine(x1, x1, x1 * attn_weight)  # Multiply each query by its corresponding attention weights, combine them with the key (and value) to form a multi-head attentive context vector, and then apply the linear layer
        return output


# Inputs to the model
x1 = torch.randn(32, 8, 56, 56)
