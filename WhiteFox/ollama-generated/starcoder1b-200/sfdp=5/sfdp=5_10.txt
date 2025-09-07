
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        query = x1.mean(-1).mean(-2)  # Compute the mean of the input and select the last dimension
        key = x1.mean(-1).mean(-2)  # Compute the mean of the input and select the last dimension
        attn_mask = torch.eye(x1.shape[-1], device=x1.device)
        attn_mask = attn_mask.unsqueeze(1).unsqueeze(0)
        attn_mask = attn_mask * (query == key)  # Apply mask to the query and key

        # Compute scaled dot product between the query and the key
        k_norm_div_s = torch.sum(attn_mask * key, dim=-1, keepdim=True) / math.sqrt(torch.prod(key.size()[:-2]))
        attn_weight = torch.softmax(attn_mask * k_norm_div_s, dim=-1)

        # Compute the dot product between the value and the attention weights
        v = query @ attn_weight  # Get the dot product between the values and the attn weights
        v = v + x1  # Add to the input
        output = torch.softmax(v, dim=-1).dropout(dropout_p) # Apply dropout to the result
        return output


# Initializing the model
m = Model()


