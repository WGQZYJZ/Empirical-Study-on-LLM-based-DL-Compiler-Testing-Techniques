
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2):
        super().__init__()
        self.matmul_qk = torch.nn.Linear(dim1 * 3, dim2)
 
    def forward(self, x1, x2, x3, query, key, value):
        qk = self.matmul_qk(torch.cat([x1, x2, x3], dim=-1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m = Model(64 * 3, 64)


