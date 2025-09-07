
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(32, 16)
 
    def forward(self, query, key):
        v_t = query * 0.5  # Multiplies the output of the attention by 0.5
        attention_v = self.attention(v_t).view(16, 16, -1)  # Performs a view operation to reshape it for softmax
        
        softmax_qkv = attention_v * scaled_qk  # Multiplies the output of the attention by the dot product between query and key tensors
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 16, 16)
x2 = torch.randn(1, 8, 32, 16)
