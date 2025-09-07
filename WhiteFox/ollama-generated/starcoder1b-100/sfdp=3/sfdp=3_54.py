
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, key_t, query_t, value_t):
        qk  = torch.matmul(query_t, key_t.transpose(-2, -1))
        scaled_qk = qk.mul(value_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=value_dropout_p)
        output = dropout_qk.matmul(x2)


# Initializing the model
m = Model()


