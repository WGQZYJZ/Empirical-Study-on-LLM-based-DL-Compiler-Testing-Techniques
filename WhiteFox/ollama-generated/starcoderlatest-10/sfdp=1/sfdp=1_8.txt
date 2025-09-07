
class Attention(torch.nn.Module):
    def __init__(self, query_channels, key_channels, value_channels):
        super().__init__()

        self.q_linear = torch.nn.Linear(query_channels, query_channels)
        self.k_linear = torch.nn.Linear(key_channels, key_channels)
        self.v_linear = torch.nn.Linear(value_channels, value_channels)

    def forward(self, x1):
        v = self.v_linear(x1)
        q = self.q_linear(x1)
        k = self.k_linear(x1)

        # Compute the dot product of query and key tensors
        qk  = torch.matmul(q, k.transpose(-2,-1)) 
        scaled_qk = qk / (float(1) ** (float(0.5 * self.attention_head_num)))

        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)

        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)
        
        # Compute the dot product of the dropout output and the value tensor
        output  = dropout_qk.matmul(v) 
        return output

# Initializing the model
a = Attention(query_channels=64, key_channels=64, value_channels=64)
q = torch.randn(1, 8, 64, 64)
k = torch.randn(1, 8, 64, 64)
v = torch.randn(1, 8, 64, 64)
