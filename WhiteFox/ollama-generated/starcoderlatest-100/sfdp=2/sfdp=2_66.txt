
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(768, 3072)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(8, 768, 30)
