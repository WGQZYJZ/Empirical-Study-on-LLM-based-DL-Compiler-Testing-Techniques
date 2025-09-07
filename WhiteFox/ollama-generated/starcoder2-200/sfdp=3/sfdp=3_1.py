
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1.0 / torch.sqrt(torch.tensor(32768))
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, query, key, value):
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)).mul_(scale)
        softmax_qk = torch.softmax(scaled_qk, dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output     = torch.matmul(dropout_qk, value)
 
        return output
# Initializing the model 
m = Model()
 
# Inputs to the model: query, key and value tensors for the attention mechanism of transformer models.
query1   = torch.randn(32768).view(-1, 64 * 8, 1)
key1     = torch.randn(32768).view(-1, 64 * 8, 1)
value1   = torch.randn(32768).view(-1, 512 * 8, 1)
 
output1  = m(query1, key1, value1)

