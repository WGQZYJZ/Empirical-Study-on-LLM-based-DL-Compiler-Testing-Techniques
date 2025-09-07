
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_conv = torch.nn.Conv2d(768, 1024, kernel_size=1)
        self.k_conv = torch.nn.Conv2d(768, 1024, kernel_size=1)
 
    def forward(self, query):
        x  = self.q_conv(query).permute(0, 3, 1, 2).contiguous()
        v  = self.k_conv(x).permute(0, 3, 1, 2).contiguous()
        qk = torch.matmul(x, v)
        scaled_qk = qk.mul(self.scale)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.p)
        output = dropout_qk.matmul(v)
        return output

# Inputs to the model
query = torch.randn(256, 768, 14, 14)
