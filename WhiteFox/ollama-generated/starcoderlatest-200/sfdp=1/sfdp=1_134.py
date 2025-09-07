
class Attention(torch.nn.Module):
    def __init__(self, d_model, d_kv=64, dropout_p=0.1):
        super().__init__()
        self.d_model = d_model
        self.d_kv = d_kv
 
        self.query_linear = torch.nn.Linear(d_model, d_kv) # Apply linear transformation to the query tensor
        self.key_linear = torch.nn.Linear(d_model, d_kv)   # Apply linear transformation to the key tensor
        self.value_linear = torch.nn.Linear(d_model, d_kv)  # Apply linear transformation to the value tensor
        self.dropout = torch.nn.Dropout2d(p=dropout_p)
 
    def forward(self, x1, x2):
        qk = self.query_linear(x1).unsqueeze(dim=-3) + self.key_linear(x2).unsqueeze(dim=-2) # Apply linear transformation to the query tensor and the key tensor
        scaled_qk = qk / math.sqrt(self.d_model)
        softmax_qk = F.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk) # Apply dropout to the softmax output
        output = dropout_qk * self.value_linear(x2).unsqueeze(-3)  # Compute the dot product of the dropout output and the value tensor
        return output.squeeze(dim=-3)
 
# Initializing the model
attention_layer1 = Attention(512, d_kv=64)
attention_layer2 = Attention(512, d_kv=64)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
