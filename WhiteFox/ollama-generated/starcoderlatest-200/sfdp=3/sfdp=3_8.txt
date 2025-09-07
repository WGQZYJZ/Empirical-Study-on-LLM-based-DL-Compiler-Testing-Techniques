
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(768, 3072)
 
    def forward(self, x1):
        qk = torch.matmul(x1, key.transpose(-2, -1)) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return x1, output


# Initializing the model
m = Model()


