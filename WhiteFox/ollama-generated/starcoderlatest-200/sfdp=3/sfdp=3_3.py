
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Linear(256, 2048) # Apply linear transformation to query tensor
        self.key_layer   = torch.nn.Linear(256, 2048) # Apply linear transformation to key tensor

    def forward(self, x1):
        k1 = self.key_layer(x1)
        qk = self.query_layer(x1)
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk.matmul(k1) # Dot product of the query and key tensor
        return output
