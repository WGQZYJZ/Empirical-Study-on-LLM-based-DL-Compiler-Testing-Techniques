
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout1 = torch.nn.Dropout(p=dropout_p) 
        self.dropout2 = torch.nn.Dropout(p=dropout_p)
        self.attention = torch.nn.MultiheadAttention(8, 3, batch_first=True)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk.mul(scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = self.dropout1(softmax_qk) 
        output = self.attention(query=self.dropout2(dropout_qk), key=key, value=value)[0] # This is different from the previous example
        return output
# Initializing the model
m = Model()


x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
x3 = torch.randn(1, 1024, 16, 16)
