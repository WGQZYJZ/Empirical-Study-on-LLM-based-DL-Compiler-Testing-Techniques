
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 64)
        self.key = torch.nn.Linear(8, 64)
 
    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        qk = torch.matmul(v1, v2.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v2)
        return output


# Initializing the model
m = Model()


def __generate_input_tensor():
    x1  = torch.randn(8, 64)
    x2  = torch.randn(64, 32)
    