
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        w1 = torch.matmul(v1, x2)
        dropout_w1 = torch.nn.functional.dropout(w1, p=0.5)
        return torch.matmul(dropout_w1, x1)


# Inputs to the model
query  = torch.randn(8, 64, 1)
key    = torch.randn(8, 64, 32)
value  = torch.randn(8, 64, 32)
