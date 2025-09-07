
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        k1 = self.conv(x1).view(x1.size(0), -1) # (batch_size, seq_len, features)
        k2 = k1 @ k1.transpose(-2, -1).contiguous().view(-1, 1, x1.shape[1], x1.shape[1]) # (seq_len, seq_len)
        attn_weight = torch.softmax(k2 / math.sqrt(x1.size(1)), dim=-1)
        output = attn_weight @ x1  # Apply dropout to the result
        return output


# Initializing the model
m = Model()


