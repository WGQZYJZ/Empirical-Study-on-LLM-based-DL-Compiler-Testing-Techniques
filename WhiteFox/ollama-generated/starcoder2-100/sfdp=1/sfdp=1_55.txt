
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1):
      	qk = torch.matmul(query1, query2)
        scaled_qk  = qk / inv_scale_factor
        softmax_qk  = scaled_qk.softmax(-1)
        dropout_qk  = softmax_qk * dropout_p
        output = dropout_qk + 1
        return output


# Initializing the model