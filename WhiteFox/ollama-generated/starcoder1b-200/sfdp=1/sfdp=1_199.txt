
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=8):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=(1, 3), stride=1)
        self.conv2 = torch.nn.Conv2d(8, 8, kernel_size=(3, 3))

        self.linear1 = torch.nn.Linear(8 * num_attention_heads, 4 * num_attention_heads)
        self.linear2 = torch.nn.Linear(4 * num_attention_heads, out_features=num_classes)

        self.attn = torch.nn.MultiheadAttention(
            num_attention_heads=num_attention_heads, dropout=dropout_p)

    def forward(self, x):
        qk = torch.matmul(x, self.key)  # Compute the dot product of the input and the key tensors
        scaled_qk = qk / math.sqrt(self.scale_factor ** float(self.num_attention_heads))  # Scale the dot product by the inverse scale factor

        attn_weights = F.softmax(scaled_qk, dim=-1)
        output = self.attn(value=x,
                          key=self.key,
                          head_mask=None,
                          attn_mask=attn_weights)[0]  # Compute the dot product of the dropout output and the value tensor

        linear1 = F.relu(self.linear1(output))
        linear2 = self.linear2(linear1)
        return linear2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
