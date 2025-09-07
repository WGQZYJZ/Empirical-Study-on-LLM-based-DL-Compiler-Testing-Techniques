
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_module = Attention(512, 3)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(x2.shape[-1]) 
        softmax_qk = torch.nn.functional.softmax(scaled_qk) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.attention_module(x1, x2, dropout_qk) # Compute attention
        return output


# Initializing the model
m = Model()
# Inputs to the model
query = torch.randn(1, 512, 768)
key = torch.randn(1, 512, 3072)
value = torch.randn(1, 512, 768)
