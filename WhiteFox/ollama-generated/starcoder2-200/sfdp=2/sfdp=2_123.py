
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_, scale_factor_=1., dropout_p=0.5):  # Input of the model
        qk = torch.matmul(query_, key_.transpose(-2, -1))
        scaled_qk = qk / (scale_factor_)  # Scale by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk.matmul(value_)
        return output


# Initializing the model