
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Parameter(torch.randn(4, 3, 8))
        self.k = torch.nn.Parameter(torch.randn(4, 3, 64, 64))
        self.v = torch.nn.Parameter(torch.randn(4, 3, 64, 64))
        self.scale_factor = torch.zeros((4, 1))
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(float(torch.pow(self.k, 2).sum()))
        scaled_qk = qk / (float(math.pi) * float(torch.pow(self.scale_factor, 0.5).sum()))
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = F.dropout(softmax_qk, p=self.p)
        output = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()


