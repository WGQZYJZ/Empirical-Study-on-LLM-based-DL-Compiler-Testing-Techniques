
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, query2, attn_mask=None):
 
        v1 = query1 @ key1.transpose(-2, -1)  # Compute the dot product of the query and key
        v1 = v1 / torch.sqrt(query1.size(-1)) 
        if attn_mask is not None:
            v1 += attn_mask
        v1 = torch.softmax(v1, dim=-1)  # Apply softmax to the result
 
        v2 = value1 @ v1  # Compute the dot product of the attention weights and the value
        
        return v2


# Initializing the model
m = Model()
 

# Inputs to the model
query_tensor1  = torch.randn(4, 3072)
key_tensor1    = torch.randn(5, 4608)
value_tensor1  = torch.randn(9, 3072)
 
query_tensor2  = torch.randn(4, 4608)
attn_mask      = torch.empty([4, 5], dtype=torch.int8).random_(0, 2).bool()
__output1__, __output2__ = m(query_tensor1, key_tensor1, value_tensor1, query_tensor2, attn_mask)

