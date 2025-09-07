
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scale_factor = torch.rsqrt((x1 ** 2).sum(-1)).unsqueeze(-1)
        softmax = (qk / scale_factor).softmax(-1)
        dropout = torch.nn.functional.dropout(softmax, p=dropout_p)
        output = dropout.matmul(value)
        return output

# Initializing the model
m = Model()

