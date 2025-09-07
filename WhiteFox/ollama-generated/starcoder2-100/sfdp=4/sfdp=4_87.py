
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, attn_mask1, value1):
        qk  = query1 @ key1.transpose(-2, -1) / math.sqrt(query1.size(-1)) # Compute the dot product of the query and key tensors, scale it by dividing by the square root of the dimensionality of the query tensor.
        qk  = qk + attn_mask1 # Add the attention mask to the scaled dot-product result.
        attn_weight1 = torch.softmax(qk, dim=-1) # Apply softmax over the dot-product result, along the last dimension. The result is a tensor with the same dimensions as the query and key tensors.
        output1  = attn_weight @ value # Compute the weighted sum of the values using the attention weights obtained in step 2.
        return output
# Initializing the model
m = Model()
 
# Input tensors to the model
query1  = torch.randn(3, 64)
key1  = torch.randn(3, 500, 64)
attn_mask1  = torch.randn(2789,)
value1  = torch.randn(2789, 64)
 
# Predicting the output using the input tensors to the model
__output__  = m(query1, key1, attn_mask1, value1)

