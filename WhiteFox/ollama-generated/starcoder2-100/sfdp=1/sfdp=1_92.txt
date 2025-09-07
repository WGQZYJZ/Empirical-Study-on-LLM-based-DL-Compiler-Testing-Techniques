

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.softmax = torch.nn.Softmax()
 
    def forward(self, query, key, value, inv_scale_factor=0.5, dropout_p=0.1, dropout_enabled=True): 
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk  = qk.div(inv_scale_factor)
 
        if not dropout_enabled:
            softmax_qk  = self.softmax(scaled_qk, dim=-1)
            return softmax_qk.matmul(value)
 
        softmax_qk  = self.softmax(scaled_qk, dim=-1)
        scaled_dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return scaled_dropout_qk.matmul(value)
