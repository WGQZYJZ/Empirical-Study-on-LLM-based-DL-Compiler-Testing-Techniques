
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.k_conv = torch.nn.Conv2d(64, 8, 1, stride=1, padding=1)
        self.v_conv = torch.nn.Conv2d(64, 32, 1, stride=1, padding=0)
 
    def forward(self, q):
        k  = self.q_conv(q).permute(0, 2, 3, 1) # Apply a pointwise convolution on the query to obtain key tensor (shape: batch_size x hidden_size x feature_dim x length of sequence in query tensor)
        v  = self.v_conv(self.k_conv(self.k)).permute(0, 2, 3, 1) # Apply a pointwise convolution on the key to obtain value tensor (shape: batch_size x hidden_size x feature_dim x length of sequence in query tensor)
        qk = torch.bmm(q, k) / math.sqrt(q.size(-1)) # Compute the scaled dot-product attention weights between q and k, and apply softmax on them (shape: batch_size x seq_len x hidden_size x feature_dim)
 
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = torch.bmm(attn_weight, v).permute(0, 3, 1, 2).contiguous() # Compute a weighted sum of value tensor (shape: batch_size x hidden_size x length of sequence in query tensor x feature_dim)
 
        return output


# Inputs to the model
q = torch.randn(64, 3, 64, 64)
