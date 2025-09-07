
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=16):
        super().__init__()
        self.query = torch.nn.Linear(576, 4096) # (B, C, H, W) --> (B, C, H*W)
        self.key = torch.nn.Linear(576, 4096) # (B, C, H, W) --> (B, C, H*W)
        self.value = torch.nn.Linear(576, 4096) # (B, C, H, W) --> (B, C, H*W)
        self.dropout = torch.nn.Dropout2d(p=dropout_p)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key(x).transpose(-2, -1)) # (B, C, H*W, H*W) --> (B, H*W, C, H*W)
        scaled_qk = qk / math.sqrt(float(4096))
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = self.dropout(softmax_qk) # (B, H*W, C, H*W) --> (B, C, H, W)
        output = torch.matmul(dropout_qk, self.value(x)) # (B, C, H, W) --> (B, C, H, W)
        return output

# Inputs to the model
