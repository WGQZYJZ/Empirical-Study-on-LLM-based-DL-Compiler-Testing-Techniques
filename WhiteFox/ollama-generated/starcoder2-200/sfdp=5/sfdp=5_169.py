
class TransformerEncoderLayer(torch.nn.Module):
    def __init__(self, d_model=512, heads=8, d_head=64, dropout=0., activation='relu'):
        super().__init__()
 
        self._layernorm = torch.nn.LayerNorm(d_model)  # Normalize the input
        self._dropout = torch.nn.Dropout(dropout)  # Dropout operation on the output
        self._activation = F.relu if activation == 'relu' else F.gelu
 
# Attention mechanism
        self._selfattn = torch.nn.MultiheadAttention(d_model, heads, dropout=0.)
 
        self._norm1 = torch.nn.LayerNorm(d_model)  # Normalize the input to the residual connection
        self._norm2 = torch.nn.LayerNorm(d_model)
 
    def forward(self, x):
 # Input
        x = self._layernorm(x)
 
# Multi-head attention
        attn1 = self._selfattn(x, x)[0]  # Compute the dot product of the input and query, and compute the result of applying the softmax
        attn2 = torch.dropout(attn1 + x, p=0., training=self._dropout.p)  # Apply dropout to the residual connection
 
# Residual block
        return self._norm2(x + attn2)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = TransformerEncoderLayer()
 
    def forward(self, x):  # Input to the encoder is a matrix that is stacked one on top of another (hence, the name of the layer). The output is the result of applying the dropout operation.
        return torch.dropout(x + self.layer1(x), p=0., training=self._dropout.p)


# Initializing the model
m = Model()
 
# Inputs to the model
input_data  = torch.rand([2,480])
__output__  = m(input_data)