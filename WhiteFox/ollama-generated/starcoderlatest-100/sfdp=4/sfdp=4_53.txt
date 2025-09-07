
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_linear = torch.nn.Linear(4, 2)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk + 1e-9, dim=-1) # Add a small positive constant to prevent the softmax from producing negative attention weights.
        output = torch.matmul(attn_weight, value)
        return output


# Inputs to the model
query  = torch.randn(4, 3, 64, 64) # Input tensor of shape [batch size, query length, input feature map heights, input feature map widths]
key    = torch.randn(2, 3, 64, 64) # Input tensor of shape [batch size, key length, input feature map heights, input feature map widths]
value  = torch.randn(2, 3, 64, 64) # Input tensor of shape [batch size, key length, input feature map heights, input feature map widths]
