
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout=0., scale_factor=1, inv_scale_factor=None, dropout_p=0.5):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        if not inv_scale_factor:
            inv_scale_factor  = scale_factor
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return dropout_qk.matmul(value), qk


# Initializing the model
m = Attention()

# Inputs to the model
query  = torch.randn(20, 32)
key    = torch.randn(512, 48)
value  = torch.randn(20, 64)

 # Compute the dot product of the query and the key
qk_without_att  = m._forward(query, key, value)[-1]
 
# Apply dropout to the softmax output, which is a scaled dot product in this scenario
dropouted_softmax = torch.nn.functional.dropout(qk_without_att.softmax(dim=-1), p=0)
 
 # Apply softmax directly instead of applying dropout first. Then the output should be identical for both cases 
 dropouted_softmax2  = qk_without_att.div(inv_scale_factor).softmax(dim=-1)
 assert (dropouted_softmax - dropouted_softmax2).abs().sum() < 0.0001
 