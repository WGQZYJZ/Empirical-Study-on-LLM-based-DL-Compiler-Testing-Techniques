
class MyModel(torch.nn.Module):
    def __init__(self, qk_input_size, attn_output_size):
        super().__init__()
        self.qk = torch.nn.Linear(qk_input_size, attn_output_size)

    def forward(self, query, key, value):  # Input: (query, key, value)
        qk = self.qk(torch.cat([query, key], dim=-1))  # Concatenate the query and the key to a single tensor
        qk = qk / torch.sqrt(torch.tensor(attn_output_size)) + 0.25 * torch.rand(query.shape)  # Normalize it and add some random noise for numerical stability
        qk += attn_mask  # Add the attention mask to this new tensor
        attn_weight = torch.softmax(qk, dim=-1)  # Compute the softmax of these values
        attn_weight *= 0.25 + 0.3 * torch.rand(attn_weight.shape)  # Add some random noise to these attention weights
        return (attn_weight @ value).view(*attn_weight.size()[:2], -1, qk_input_size).sum(-2)  # Compute the dot product of these attention weights and the values


qk = self.qk(torch.cat([query, key], dim=-1))  # Concatenate the query and the key to a single tensor
qk = qk / torch.sqrt(torch.tensor(attn_output_size)) + 0.25 * torch.rand(query.shape)  # Normalize it and add some random noise for numerical stability
qk += attn_mask  # Add the attention mask to this new tensor
attn_weight = torch.softmax(qk, dim=-1)  # Compute the softmax of these values
attn_weight *= 0.25 + 0.3 * torch.rand(attn_weight.shape)  # Add some random noise to these attention weights


# Initializing the model
qk_input_size = qk.size(-1).item()
attn_output_size = attn_weight.size(-1).item()
m = MyModel(qk_input_size, attn_output_size)


