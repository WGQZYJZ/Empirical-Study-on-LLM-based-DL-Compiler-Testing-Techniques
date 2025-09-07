
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1))
        inv_scale_factor = qk.div(torch.sqrt(torch.pow(qk.shape[-2], 2) + torch.pow(qk.shape[-1], 2)))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 64, 64, requires_grad=True)
x2  = torch.randn(8, 64, 64, requires_grad=True)
