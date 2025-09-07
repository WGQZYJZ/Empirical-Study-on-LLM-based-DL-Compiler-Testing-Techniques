
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_key = torch.nn.Linear(3, 16)
 
    def forward(self, qk):
        qk = self.query_key(qk)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.randn(16, 3, 256, 256)
