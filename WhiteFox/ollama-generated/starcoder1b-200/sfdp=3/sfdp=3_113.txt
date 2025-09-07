
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) * scale_factor
        dropout_qk = F.dropout(qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
