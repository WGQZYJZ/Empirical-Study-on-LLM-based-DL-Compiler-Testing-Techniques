
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(value)
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.self_attention = SelfAttention()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        attention_output = self.self_attention(v1, v1, v1)
        v6 = torch.cat([attention_output, v1], dim=-1)  # Concatenate the output of the convolutional layer with itself and reshape them to a 5D tensor so they can be passed into the fully-connected layer as input
        