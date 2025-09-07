
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
 
        self.q = torch.nn.Linear(d_model, d_model)
        self.k = torch.nn.Linear(d_model, d_model)
        self.v = torch.nn.Linear(d_model, d_model)
 
    def forward(self, query): # The input tensor
        q = self.q(query).view(-1, self.num_heads, self.d_model // self.num_heads)
        k = self.k(query).view(-1, self.num_heads, self.d_model // self.num_heads)
        v = self.v(query).view(-1, self.num_heads, self.d_model // self.num_heads)
 
        qk = torch.matmul(q, k.transpose(-2, -1))  # The attention scores matrix
        scale_factor = 1 / math.sqrt(self.d_model)
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)  # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, v)  # Compute the dot product of the dropout output and the value
 
        return output
 
m = MultiHeadAttention(512, 8)
 
x = torch.randn(2048, 512)  # The input tensor
