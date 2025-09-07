
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 128)
        self.key   = torch.nn.Linear(768, 128)
        self.value = torch.nn.Linear(128, 256)
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x):
        # Get query and key tensors for pointwise convolutions
        q = self.query(x).view(-1, x.size(1))
        k = self.key(x).view(-1, x.size(1), 1).expand_as(q)
        # Scale the dot-product attention (QK @ KT) with a mask for preventing it to attend to certain positions
        attn_mask = torch.triu(torch.ones_like(q, dtype=torch.uint8))
        # Compute the weighted sum of `value` and `key` vectors
        # The weights should be non-negative because otherwise they will be added together as the dot-product
        # This is equivalent to computing `(v^T @ k) / ||k||` where v^T = value, k = key.transpose(-2,-1).
        scaled_attention = torch.bmm(attn_weight, value)
        # Apply dropout if needed
        if not self.training:
            return output * attn_mask  # Add attention mask to the result
        else:
            # The scaled dot-product will be applied on a per-sample basis and hence it will take all positive entries to the dot-product
            return output * (scaled_attention.softmax(dim=-1))  # Apply dropout and softmax over the result


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 768)
