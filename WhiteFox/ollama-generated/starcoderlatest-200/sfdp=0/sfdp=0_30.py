
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(768, 1024)
        self.linear_k = torch.nn.Linear(768, 1024)
        self.linear_v = torch.nn.Linear(768, 1024)
        self.scale = torch.nn.Parameter(torch.ones(1))
 
    def forward(self, x):
        q  = self.linear_q(x).transpose(-2, -1) # [batch, head_num, seq_len, dim] --> [seq_len, batch * head_num, dim]
        k  = self.linear_k(x).transpose(-2, -1) # [batch, head_num, seq_len, dim] --> [seq_len, batch * head_num, dim]
        v  = self.linear_v(x).transpose(-2, -1) # [batch, head_num, seq_len, dim] --> [seq_len, batch * head_num, dim]
 
        scaled_dot_product = torch.matmul(q, k) / self.scale
        attention_weights = torch.softmax(scaled_dot_product, dim=-1).type(torch.float32) # softmax to compute attention weights

        output  = torch.matmul(attention_weights, v) # [seq_len, batch * head_num, dim] --> [batch, head_num, seq_len, dim]
        output = output.transpose(1, 2).contiguous()  # [batch, head_num, seq_len, dim] --> [batch, seq_len, head_num, dim]
        return output, attention_weights


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.transformer = TransformerBlock()
 
    def forward(self, x1):
        output, attention_weights  = self.transformer(x1)
        return output


# Initializing the model
m = Model()


