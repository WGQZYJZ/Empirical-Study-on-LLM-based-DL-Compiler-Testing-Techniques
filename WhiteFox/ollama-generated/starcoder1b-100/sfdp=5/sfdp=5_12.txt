
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        query = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        key   = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        attn_mask  = torch.ones(query.size()).cuda() + (torch.rand_like(attn_mask) < 0.9).type_as(query) # Compute the attention mask for each of the query and key dimensions, and scale it between 0 to 1
        attn_weight = torch.softmax(attn_mask, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        value = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        output = (attn_weight @ value).squeeze(-2) # Squeeze the result of the dot product by the batch dimension
        return output


# Initializing the model
m = Model()


