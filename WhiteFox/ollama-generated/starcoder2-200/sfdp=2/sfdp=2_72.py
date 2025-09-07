
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        # Compute the dot product of the query and the key
        qk  = torch.matmul(query, key.transpose(-2, -1))
        # Scale the dot product by the inverse scale factor
        scaled_qk  = qk.div(inv_scale_factor)
        # Apply softmax to the scaled dot product
        smk  = scaled_qk.softmax(dim=-1)
        # Apply dropout to the softmax output
        dropok  = torch.nn.functional.dropout(smk, p=dropout_p)
        return dropok @ value


# Initializing the model
attn_model  = Attention()
 
# Input tensors for query and key: shape (batch size x sequence length) of floats
key  = torch.randn((320, 512))
query  = torch.randn(32, 480)
value  = torch.randn((32, 768))
 
# Scaled dot product attention with dropout
output_from_model__att = attn_model(query, key, value)

