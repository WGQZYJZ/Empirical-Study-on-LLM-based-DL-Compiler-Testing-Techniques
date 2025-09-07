
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Apply the convolution to the input tensor
        qk = torch.matmul(v1, v1.transpose(-2, -1))  # Compute the dot product of v1 and v1.transpose(0,1)
        v2 = torch.nn.functional.dropout(qk / math.sqrt(self.attention_head_size), p=dropout_p)
        v3 = qk * v2
        return v3


# Initializing the model
m = Model()


