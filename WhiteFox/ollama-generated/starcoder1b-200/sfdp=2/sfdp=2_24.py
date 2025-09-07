
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        qk = torch.matmul(query, key.transpose(-2, -1)) / scale_factor
        scaled_qk = qk.div_(scale_factor)
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p, training=training)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


