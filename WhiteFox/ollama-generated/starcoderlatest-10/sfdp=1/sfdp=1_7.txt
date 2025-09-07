
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 1024)
 
    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) * 3
        qk = qk.div(inv_scale_factor)
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x3)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
q  = torch.randn(1, 768, 512, 800)
k  = torch.randn(1, 768, 512, 800)
v  = torch.randn(1, 768, 512, 800)

 