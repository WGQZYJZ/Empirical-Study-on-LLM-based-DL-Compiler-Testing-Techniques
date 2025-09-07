
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key):
        # Apply convolution to the query and key tensor
        qk = self.query_conv(query)
        kq = self.key_conv(key)
 
        # Compute the dot product of the query and key, scale it
        qk = qk @ torch.transpose(self.key_conv.weight, -1, -2).float() / math.sqrt(self.query_conv.in_channels * 3 * self.key_conv.kernel_size[0] * self.key_conv.kernel_size[1])
 
        # Add the attention mask to the scaled dot product
        qk = qk + torch.tensor([[[[-1., -1., -1., -1., -1.], [-1., -1., -1., -1., -1.], [-1., -1., -1., -1., -1.]]]])
 
        # Compute softmax on the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)
 
        # Multiply the output of the convolution by the attention weights
        value = self.key_conv(attn_weight) @ torch.transpose(self.value_conv.weight, -1, -2).float() / math.sqrt(self.query_conv.in_channels * 3 * self.value_conv.kernel_size[0] * self.value_conv.kernel_size[1])
        return value


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 32, 32)
