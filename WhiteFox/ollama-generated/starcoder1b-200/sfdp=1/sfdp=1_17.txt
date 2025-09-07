
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        k1 = self.conv(x1).view(x1.shape[0], -1)
        k2 = self.conv(x2).view(-1, x2.shape[-1])
        qk = torch.matmul(k1, k2.transpose(-2, -1))
        k_scaled = qk / math.sqrt(float(m.kernel_size[0] * m.kernel_size[0]))
        scaled_qk = k_scaled * math.sqrt(scale_factor)
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        value = dropout_qk.matmul(x2).view(batch, x2.shape[0], -1)
        return value


# Initializing the model
m = Model()

