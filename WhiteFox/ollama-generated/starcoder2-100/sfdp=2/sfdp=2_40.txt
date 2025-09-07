
class Model(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
 
        self.key = torch.nn.Parameter(torch.randn(32*num_heads, 64))
        self.query = torch.nn.Parameter(torch.randn(10*num_heads, 64))
        self.value = torch.nn.Parameter(torch.randn(32*num_heads, 64))
        self.scale_factor = 50
 
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout  = torch.nn.Dropout(p=0.1)

    def forward(self, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
 
        scaled_qk = qk.div(self.scale_factor) 
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
 
        output  = dropout_qk @ value
        return output

# Initializing the model