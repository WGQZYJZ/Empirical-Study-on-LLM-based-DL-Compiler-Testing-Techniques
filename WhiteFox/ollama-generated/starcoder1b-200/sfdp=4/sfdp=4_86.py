
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_proj = torch.nn.Linear(768, 512)
        self.value_proj = torch.nn.Linear(768, 512)

    def forward(self, x):
        batch_size = x.shape[0]

        # The first and second dimension are spatial dimensions of images. 
        query = x
        key = torch.randn_like(x)
        value = torch.randn_like(x)
        attn_mask = (query != 0).unsqueeze(-1).unsqueeze(-1) # Create an attention mask to make it possible for the model to use information from future words.
        key_proj = self.key_proj(key)  # Compute the weighted average of the keys with respect to the keys projected into query's embedding space.
        value_proj = self.value_proj(value) # Compute the weighted average of values with respect to values projected into the output space.

        attn_weights = torch.bmm(query, key_proj.transpose(-2, -1))  # Compute the dot product between query and key, then compute softmax over the result to get attention weights.
        attn_weights = attn_weights / math.sqrt(key_proj.size(-1)) # Normalize the weights using standard normal distribution.
        attn_output = torch.bmm(attn_weights, value)  # Compute the weighted sum of values and the values projected into the output space.
        attn_output = attn_output + attn_mask.unsqueeze(-1).unsqueeze(-1)  # Add an attention mask to the output so that it can be used for future computation.

        return attn_output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3, 8, 64, 64)
