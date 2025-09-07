
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(64, 128)
        self.value = torch.nn.Linear(128, 64)
        self.query = torch.nn.Linear(64, 32)
 
    def forward(self, query, value):
        attn_out = F.softmax(self.attn(torch.cat([query, value], dim=0)), dim=-1) # Compute the attention weights using the linear combination of the query and key tensors
        output = torch.bmm(attn_out, self.value(value))  # Apply a matrix multiplication between the attention weights and the values
        return output


# Inputs to the model
x1 = torch.randn(32, 64)  # A tensor with shape [batch_size x num_heads x qkv_dim] for queries/keys/values
x2 = torch.randn(32, 64)  # Another tensor with shape [batch_size x num_heads x kdim]. Note that it can be of a different length than the first one. In this case, the extra dimensions will broadcast properly.
