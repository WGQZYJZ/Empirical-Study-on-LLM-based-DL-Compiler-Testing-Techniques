
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2, query, key):
        qk = self.attn(query, key, value)[0] # Apply multi-headed attention and compute the output tensor of attention mechanism
        scaled_qk = qk / math.sqrt(float(key.size(-1))) # Scale the dot product by a sqrt of the dimension of each tensor in a batch of examples 
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        output = torch.nn.functional.dropout(softmax_qk, p=0.15)  # Dropout is applied after applying softmax so that attention weights in each heads do not get too large
        return output
