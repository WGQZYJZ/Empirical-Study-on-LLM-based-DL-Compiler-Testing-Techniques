
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query_, key_, value_=None):
        # Compute the dot product between the query and keys tensors
        scaled = torch.matmul(query_, torch.transpose(key_, -2, -1)) * inv_scale_factor

        # Apply softmax to scale down large values without saturating the output
        normalized = scaled.softmax(-1)

        # Apply dropout to randomly remove the values in each row of the output
        dropouted = torch.nn.functional.dropout(normalized, p=0.5)

        # Compute the dot product between the output and value tensor
        if value_ is not None:
            return dropouted @ value_.transpose(-2,-1).contiguous()


# Initializing the model
m  = Model()

# Input tensors to the model
query_tensor  = torch.randn(batch, query_size)
key_tensor   = torch.randn(batch, key_size)
value_tensor  = torch.randn(batch, key_size)

