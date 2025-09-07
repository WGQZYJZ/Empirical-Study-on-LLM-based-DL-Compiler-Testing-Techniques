
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2):
        v1, attention_weights = self.attention(x1, x2, x2) # Apply multi-head attention and store the attention weights in attention_weights
        v6  = torch.matmul(v1, x2.transpose(-2,-1)) # Compute the dot product of the output of the multi-head attention and the value tensor
        return v6
