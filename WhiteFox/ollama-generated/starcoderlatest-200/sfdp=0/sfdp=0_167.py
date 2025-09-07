
class Attention(torch.nn.Module):
    def __init__(self, dim_head=None):
        super().__init__()
        self.dim_head = dim_head
 
    def forward(self, q, k, v, mask=None):
        dots = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.dim_head)  # (batch_size, head_num, query_length, key_length)
        if mask is not None:
            dots.masked_fill_(mask == 0, float('-inf'))
 
        attention_weights = dots.softmax(dim=-1)  # (batch_size, head_num, query_length, key_length)
        output = attention_weights.matmul(v)  # (batch_size, head_num, query_length, value_length)

        return output, attention_weights


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = Attention()
 
    def forward(self, q1, k1, v1, q2, k2, v2, mask=None):
        output, attention_weights  = self.att(q1, k1, v1, mask)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1  = torch.randn(3, 64, 512, 8)  # (batch_size, query_length, input_length, dim_per_head)
k1  = torch.randn(3, 64, 2048, 8)  # (batch_size, key_length, input_length, dim_per_head)
v1  = torch.randn(3, 64, 2048, 8)  # (batch_size, value_length, input_length, dim_per_head)
q2  = torch.randn(3, 512, 2048, 8)  # (batch_size, query_length, key_length, dim_per_head)
k2  = torch.randn(3, 512, 2048, 8)  # (batch_size, key_length, key_length, dim_per_head)
v2  = torch.randn(3, 512, 2048, 8)  # (batch_size, value_length, value_length, dim_per_head)
