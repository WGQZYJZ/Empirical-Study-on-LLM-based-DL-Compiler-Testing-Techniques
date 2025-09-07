
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.qk  = torch.nn.Linear(d_model, d_key)
 
    def forward(self, q, k, v):
            scaled_qk = self.qk(q).div_(inv_scale_factor)
            softmax_qk = scaled_qk.softmax(-1) 
            dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
            return dropout_qk.matmul(v)


# Initializing the model