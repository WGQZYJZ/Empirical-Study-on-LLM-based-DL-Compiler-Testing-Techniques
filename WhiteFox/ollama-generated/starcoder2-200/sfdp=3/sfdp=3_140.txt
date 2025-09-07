
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.rand(()) + 1e-8
        self.dropout = torch.rand(()).clamp_(0., 1.)
        self.key = torch.randn((32, 64))
        self.value = torch.randn((32, 512))
        self.query = torch.randn((32, 512))
 
    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1) * scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk.matmul(value)


# Initializing the model