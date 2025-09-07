
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm1 = LayerNorm()
        self.layer_norm2 = LayerNorm()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.maxpool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
 
    def forward(self, x):
        qk = torch.matmul(x[:, :, :-1, :], x[:, :, 1:, :].transpose(-2, -1))
        scale_factor = torch.rsqrt((qk[:, :, :, :, :, :] + 1e-16).sum(dim=-1)[:, None])
        scaled_qk = qk.div(scale_factor[:, :, None, None])
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        x = self.layer_norm1(x) + dropout_qk.matmul(value[:, :, :, :, None])  # input: batch x sequence_length x input_size x input_size
        x = self.layer_norm2(x) + torch.matmul(dropout_qk, value)  # input: batch x sequence_length x attention_head x attention_head

# Initializing the model
m = Model()

