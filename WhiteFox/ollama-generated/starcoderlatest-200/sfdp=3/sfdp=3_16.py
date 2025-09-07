
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, query_scale=4., dropout_p=0.5, num_attn_layers=6):
        super().__init__()

        self.num_heads = num_heads
        self.query_scale = query_scale
 
        self.attns = nn.ModuleList(nn.MultiheadAttention(num_attention_heads=self.num_heads) for _ in range(num_attn_layers))

    def forward(self, q1, k1, v1):
        attns = []
        for i, (atn, k1_, v1_) in enumerate(zip(self.attns, k1, v1)):
            out1, attention_weights1 = atn(q1, k1_, v1_)
            if i == 0:
                attn1 = out1

            attns.append(attention_weights1)
        return torch.cat([attn1], dim=1), attns

    def multihead_matmul(self, q1, k1, v1):
        qk = self.dot_product_attention(q1, k1)
        return self.dropout(qk)

class Model(torch.nn.Module):
    def __init__(self, num_heads=8, query_scale=4., dropout_p=0.5, num_attn_layers=6):
        super().__init__()

        self.num_heads = num_heads
        self.query_scale = query_scale
 
        self.attns = nn.ModuleList(nn.MultiheadAttention(num_attention_heads=self.num_heads) for _ in range(num_attn_layers))

    def forward(self, q1, k1, v1):
        attns = []
        for i, (atn, k1_, v1_) in enumerate(zip(self.attns, k1, v1)):
            out1, attention_weights1 = atn(q1, k1_, v1_)
            if i == 0:
                attn1 = out1

            attns.append(attention_weights1)
        return torch.cat([attn1], dim=1), attns

    def dot_product_attention(self, q1, k1):
        qk = self._scaled_dot_product_attention(q1, k1)

        softmax_qk = qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        return self._dropout_layer(dropout_qk)

    def _scaled_dot_product_attention(self, q1, k1):
        dot_product = torch.matmul(q1, k1.transpose(-2, -1))

        # Scale the dot product by a factor
        scaled_qk = dot_product.mul(self.query_scale)  # qk
        return scaled_qk

    def _dropout_layer(self, x):
        # Apply dropout to the output of the convolution
        return torch.nn.functional.dropout(x, p=self.dropout_p)


# Inputs to the model
q1 = torch.randn(1, 3, 64, 64)
k1 = torch.randn(2, 3, 64, 64)
v1 = torch.randn(2, 3, 64, 64)
__output__, attns_list = m(q1, k1, v1)

