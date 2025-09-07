

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(128, 3)
 
    def forward(self, query, key):
        value = torch.randn((query.size()[0], 3))
        v_shape = value.size()
 
        inv_scale_factor = 64 # Constant
        scale_factor = 0.75 # Variable
        dropout_p = 2e-1 # Variable
        dropout_mask = torch.ones(v_shape) # Tensor
        query, key = map(lambda x: self.matmul(x), (query, key))
        qk = torch.matmul(query, key.transpose(-2,-1))
        scaled_qk = qk / inv_scale_factor
 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        # We use the same mask here to ensure dropout always masks out the value tensors
        dropout_mask[:, 0] = 0.8
 
        masked_output  = torch.masked_select(softmax_qk * dropout_mask, torch.ones_like(softmax_qk))
        masked_value   = torch.masked_select(value, torch.ones_like(value))
        output         = torch.nn.functional.one_hot(masked_output, 3)
        return torch.matmul(output, masked_value).view(-1), qk
 
m = Model()

