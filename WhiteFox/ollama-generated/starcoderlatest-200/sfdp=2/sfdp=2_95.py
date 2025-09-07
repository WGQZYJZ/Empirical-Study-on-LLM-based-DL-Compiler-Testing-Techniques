
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn1 = Attention()
        self.attn2 = Attention()
 
    def forward(self, x1, x2):
        out1 = self.attn1(x1, x2)  # Compute the output of attention1 with an input tensor and a key tensor
        out2 = self.attn2(out1, x2)  # Compute the output of attention2 with an input tensor and a key tensor
        return out2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 3, 256, 256)
x2 = torch.randn(16, 8, 256, 256)
